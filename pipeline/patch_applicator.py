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
                if i == failure.detected_fault.client_line_number - 1:
                    patched_content += "// TODO: review this AI generated patch!\n"
                    patched_content += patch.value + "\n"
                if (i < failure.detected_fault.client_line_number - 1) or i > failure.detected_fault.client_end_line_number:
                    patched_content += row

            f.close()
            return patched_content
