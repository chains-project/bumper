import os
import subprocess

from pipeline.types.failure import Failure
from pipeline.types.patch import Patch
from pipeline.types.project import Project


class PatchApplicator:
    def __init__(
            self,
            project: Project
    ):
        self.project = project

    def get_patched_content(self, patch: Patch, failure: Failure) -> str:
        file_path = failure.detected_fault.error_info.client_file_path
        absolute_path = f"{self.project.path}{file_path}"
        patched_content = ""
        with open(absolute_path, "r") as f:
            for i, row in enumerate(f, 1):
                if i == failure.detected_fault.client_line_number:
                    patched_content += "// TODO: review this AI generated patch!\n"
                    patched_content += patch.value + "\n"
                if (i < failure.detected_fault.client_line_number) or i > failure.detected_fault.client_end_line_number:
                    patched_content += row

            f.close()
            return patched_content

    def save_patched_code(self, patch: Patch, failure: Failure):
        patched_code_path = self.get_patched_code_path(patch, failure)
        os.makedirs(os.path.dirname(patched_code_path), exist_ok=True)

        subprocess.run([
            'cp', "-r",
            f"{self.project.path}/{self.project.project_name}/",
            f"{self.project.path}/patched_code/{patch.id}/{self.project.project_name}"
        ], stdout=subprocess.PIPE)

        subprocess.run([
            'ln', '-s',
            f"{self.project.path}/{self.project.library_name}-{self.project.old_library_version}.jar",
            f"{self.project.path}/patched_code/{patch.id}/{self.project.library_name}-{self.project.old_library_version}.jar"
        ], stdout=subprocess.PIPE)

        subprocess.run([
            'ln', '-s',
            f"{self.project.path}/{self.project.library_name}-{self.project.new_library_version}.jar",
            f"{self.project.path}/patched_code/{patch.id}/{self.project.library_name}-{self.project.new_library_version}.jar"
        ], stdout=subprocess.PIPE)

        file_path = failure.detected_fault.error_info.client_file_path
        file_absolute_path = f"{self.project.path}/patched_code/{patch.id}{file_path}"
        with open(file_absolute_path, "w") as f:
            f.write(self.get_patched_content(patch, failure))
            f.close()

    def get_patched_code_path(self, patch: Patch, failure: Failure):
        return f"{self.project.path}/patched_code/{patch.id}/{self.project.project_name}"
