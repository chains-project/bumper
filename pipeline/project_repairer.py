import copy
import os
import subprocess

from pipeline.failure_extractor import FailureExtractor
from pipeline.patch_applicator import PatchApplicator
from pipeline.patch_generator_service import PatchGeneratorService, PipelineRunningMode
from pipeline.types.failure import Failure
from pipeline.types.llm import LLMType
from pipeline.types.patch import Patch

from pipeline.types.project import Project
from pipeline.types.project_repair_status import ProjectRepairStatus
from pipeline.types.prompt import Prompt


class ProjectRepairer:
    def __init__(self, project: Project, pipeline: PipelineRunningMode = PipelineRunningMode.STANDARD,
                 model: LLMType = LLMType.GEMINI):
        self.project = project
        self.pipeline = pipeline
        self.model = model

    def repair(self) -> ProjectRepairStatus:
        base_path = self.project.path

        extractor = FailureExtractor(self.project)
        failures = extractor.get_failures(base_path=base_path)
        print(f"found {len(failures)} failures!")

        if len(failures) <= 0:
            return ProjectRepairStatus(repaired=True)

        failure = failures[0]
        patches = []

        for trial_count in range(1, os.getenv("MAX_TRIES_TO_REPAIR", 10) + 1):
            try:
                patch = self.generate_patch(failure=failure)
                result = self.check_for_validity(patch=patch, failure=failure)

                if self.is_success(result):
                    print("Project patched!")
                    patches.append(patch.id)
                    return ProjectRepairStatus(fixed_errors_count=1, generated_patch_count=trial_count, repaired=True,
                                               patches=patches, initial_errors_count=len(failures))
                else:
                    print("Project not patched, trying to understand if it patched the specific failure:")

                    if patch.force_validation is False:
                        print(f"Before we have {len(failures)} failures")
                        new_failures = extractor.get_failures(base_path=f"{base_path}/patched_code/{patch.id}")
                        if len(new_failures) <= 0:
                            print("Error extracting new failures, patch is not valid.")
                            continue
                        print(f"Now we have {len(new_failures)} failures")
                    else:
                        print("Patch is forcing validation = True!")
                        new_failures = []

                    if len(new_failures) < len(failures):
                        print("Failure is fixed, we can continue from here")
                        patches.append(patch.id)
                        new_project = copy.deepcopy(self.project)
                        new_project.root_project = self.project.root_project or self.project
                        new_project.path = self.project.path + f"/patched_code/{patch.id}"
                        repairer = ProjectRepairer(project=new_project, pipeline=self.pipeline, model=self.model)
                        return ProjectRepairStatus(
                            fixed_errors_count=1,
                            generated_patch_count=trial_count,
                            repaired=True,
                            patches=patches,
                            initial_errors_count=len(failures)
                        ).merge(repairer.repair())
                    else:
                        print("Failure not fixed, trying to generate new patch")
            except KeyboardInterrupt:
                exit(1)
            except:
                print("Failure in running the last repair round, skipping.")

        print(f"Repair failed for this failure (#{failure.detected_fault.identifier})")
        return ProjectRepairStatus(
            fixed_errors_count=0,
            generated_patch_count=os.getenv("MAX_TRIES_TO_REPAIR", 10) + 1,
            repaired=False,
            patches=patches,
            initial_errors_count=len(failures)
        )

    def generate_patch(self, failure: Failure) -> Patch:
        try:
            patch_generator = PatchGeneratorService.get_generator(failure=failure, project=self.project,
                                                                  pipeline=self.pipeline, model=self.model)
            print(f"Generating patch for project {self.project.project_name}")
            patch = patch_generator.generate()
            patch_generator.save_patch(patch)
            print("Patch generated")
            return patch
        except KeyboardInterrupt:
            exit(1)
        except:
            print("Failing to generate the patch.")
            raise

    def check_for_validity(self, patch: Patch, failure: Failure) -> subprocess.CompletedProcess:
        patch_applicator = PatchApplicator(self.project)
        patch_applicator.save_patched_code(patch, failure)
        print("File patched")
        print("Checking for validity...")

        try:
            result = subprocess.run([
                'bash',
                'benchmarks/bump/scripts/test_patched_code.sh',
                self.project.project_id,
                patch_applicator.get_patched_code_path(patch, failure)
            ], timeout=300, stdout=subprocess.PIPE)
            return result
        except subprocess.TimeoutExpired:
            print("[ERROR] test_patched_code.sh timed out! Cleaning up before continuing...")
            subprocess.run([
                'bash',
                'benchmarks/bump/scripts/cleanup_after_failure.sh',
                self.project.project_id,
            ], stdout=subprocess.PIPE)

        return subprocess.CompletedProcess(returncode=1)

    def is_success(self, result: subprocess.CompletedProcess) -> bool:
        return True if result.returncode == 0 else False
