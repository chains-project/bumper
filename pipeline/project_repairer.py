import copy
import subprocess

from pipeline.failure_extractor import FailureExtractor
from pipeline.patch_applicator import PatchApplicator
from pipeline.patch_generator_service import PatchGenerator
from pipeline.types.project import Project
from pipeline.types.prompt import Prompt


class ProjectRepairer:
    def __init__(self, project: Project):
        self.project = project

    def repair(self, from_patch_id=None) -> bool:
        base_path = f"{self.project.path}/patched_code/{from_patch_id}" if from_patch_id else self.project.path

        extractor = FailureExtractor(self.project)
        failures = extractor.get_failures(base_path=base_path)
        print(f"found {len(failures)} failures!")

        if len(failures) <= 0:
            return True

        failure = failures[0]
        for _ in range(0, 5):
            prompt = Prompt(
                template="complete_instructions_on_top",
                values={
                    "in_class_client_code": failure.detected_fault.in_class_code,
                    "client_code": failure.detected_fault.method_code,
                    "error_message": failure.detected_fault.error_info.error_message,
                    "additional_info": failure.detected_fault.error_info.additional_info,
                    "bump_description": failure.get_api_diff(project_id=self.project.project_id)
                }
            )
            patch_generator = PatchGenerator()
            print(f"Generating patch for project {self.project.project_name}")
            patch = patch_generator.generate(prompt)
            self.project.save_patch(patch, prompt=prompt, failure=failure)
            patch_applicator = PatchApplicator(self.project)
            patch_applicator.save_patched_code(patch, failure)
            print("File patched")
            print("Checking for validity...")
            result = subprocess.run([
                'sh',
                'benchmarks/bump/scripts/test_patched_code.sh',
                self.project.project_id,
                patch_applicator.get_patched_code_path(patch, failure)
            ], stdout=subprocess.PIPE)
            if result.returncode == 0:
                print("Failure patched!")
                return True
            else:
                print("Project not patched, trying to understand if it patched the specific failure:")
                print(f"Before we have {len(failures)} failures")

                new_failures = extractor.get_failures(base_path=f"{base_path}/patched_code/{patch.id}")
                if len(new_failures) <= 0:
                    print("Error extracting new failures, cannot repair project")
                    return False

                print(f"Now we have {len(new_failures)} failures")
                if len(new_failures) < len(failures):
                    print("Failure is fixed, we can continue from here")
                    new_project = copy.deepcopy(self.project)
                    new_project.path = self.project.path + f"/patched_code/{patch.id}"
                    repairer = ProjectRepairer(project=new_project)
                    return repairer.repair()
                else:
                    print("Failure not fixed, trying to generate new patch")

        print(f"Repair failed for this failure (#{failure.detected_fault.identifier})")
        return False
