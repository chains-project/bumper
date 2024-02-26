import subprocess

from pipeline.failure_extractor import FailureExtractor
from pipeline.patch_applicator import PatchApplicator
from pipeline.patch_generator import PatchGenerator
from pipeline.types.project import Project
from pipeline.types.prompt import Prompt


class ProjectRepairer:
    def __init__(self, project: Project):
        self.project = project

    def repair(self, from_patch_id=None) -> bool:
        base_path = f"{self.project.path}/patched_code/{from_patch_id}" if from_patch_id else self.project.path

        extractor = FailureExtractor(self.project)
        failures = extractor.get_failures(base_path=base_path)

        if len(failures) <= 0:
            return True

        failure = failures[0]
        for run in range(0, 5):
            prompt = Prompt(
                template="complete_instructions_on_top",
                values={
                    "in_class_client_code": failure.detected_fault.in_class_code,
                    "client_code": failure.detected_fault.method_code,
                    "error_message": failure.detected_fault.error_info.error_message,
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
                print("Failure not patched, trying again...")

        print(f"Repair failed for this failure (#{failure.detected_fault.identifier})")
        return False
