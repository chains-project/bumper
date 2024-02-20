import os

from pipeline.types.patch import Patch
from pipeline.types.prompt import Prompt


class Project:
    def __init__(
            self,
            project_id: str,
            project_name: str,
            path: str,
            library_name: str,
            old_library_version: str,
            new_library_version: str,
            library_group_id: str = ""
    ) -> None:
        self.library_group_id = library_group_id
        self.project_name = project_name
        self.project_id = project_id
        self.path = path
        self.library_name = library_name
        self.old_library_version = old_library_version
        self.new_library_version = new_library_version

    def save_patch(self, patch: Patch, prompt: Prompt = None):
        filename = f"prompts/{prompt.template}/{patch.id}.txt" if prompt is not None else f"others/{patch.id}.txt"
        path = f"{self.path}/patches/{filename}"
        os.makedirs(os.path.dirname(path), exist_ok=True)

        with open(path, "w") as f:
            f.write(patch.value)
            f.close()

        if prompt is not None:
            with open(f"{self.path}/patches/prompts/{prompt.template}/{patch.id}_prompt.txt", "w") as f:
                f.write(prompt.get_text())
                f.close()
