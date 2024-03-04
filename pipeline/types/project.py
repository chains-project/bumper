import json
import os

from pipeline.types.failure import Failure
from pipeline.types.patch import Patch
from pipeline.types.prompt import Prompt


class Project:

    @staticmethod
    def from_bump(bump_folder: str, project_id: str):
        with open(f"{bump_folder}/filtered_data/{project_id}.json", "r") as f:
            data = json.load(f)
            return Project(
                project_id,
                project_name=data["project"],
                path=f"{bump_folder}/clients/{project_id}",
                library_name=data["updatedDependency"]["dependencyArtifactID"],
                library_group_id=data["updatedDependency"]["dependencyGroupID"],
                old_library_version=data["updatedDependency"]["previousVersion"],
                new_library_version=data["updatedDependency"]["newVersion"]
            )
    
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

    def save_patch(self, patch: Patch, prompt: Prompt, failure: Failure = None):
        filename = f"prompts/{prompt.template}/{patch.id}/patch.txt"
        path = f"{self.path}/patches/{filename}"
        os.makedirs(os.path.dirname(path), exist_ok=True)

        with open(path, "w") as f:
            f.write(patch.value)
            f.close()

        with open(f"{self.path}/patches/prompts/{prompt.template}/{patch.id}/prompt.txt", "w") as f:
            f.write(prompt.get_text())
            f.close()

        if failure is not None:
            with open(f"{self.path}/patches/prompts/{prompt.template}/{patch.id}/original.txt", "w") as f:
                f.write(failure.detected_fault.method_code)
                f.close()

    def get_metadata(self) -> dict:
        path = f"{self.path}/metadata.json"
        if os.path.exists(path=path):
            with open(path, "r") as f:
                result = json.loads(f.read())
                f.close()
                return result
        
        return {
            "repaired": False
        }

    def save_metadata(self, meta: dict = {"successful": False}):
        with open(f"{self.path}/metadata.json", "w") as f:
            f.write(json.dumps(meta))
            f.close()
            
