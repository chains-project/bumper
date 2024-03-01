from abc import ABC, abstractmethod
import json
import os

from pipeline.types.failure import Failure
from pipeline.types.patch import Patch
from pipeline.types.project import Project

class PatchGenerator(ABC):
    def __init__(self, failure: Failure, project: Project) -> None:
        super().__init__()
        self.failure = failure
        self.project = project

    @abstractmethod
    def generate() -> Patch:
        pass
        
    def save_patch(self, patch: Patch):
        filename = f"{patch.id}/patch.txt"
        path = f"{self.project.path}/patches/{filename}"
        os.makedirs(os.path.dirname(path), exist_ok=True)

        with open(path, "w") as f:
            f.write(patch.value)
            f.close()

        with open(f"{self.project.path}/patches/{patch.id}/original.txt", "w") as f:
            f.write(self.failure.detected_fault.method_code)
            f.close()

        with open(f"{self.project.path}/patches/{patch.id}/failure.json", "w") as f:
            f.write(json.dumps(self.failure.__dict__))
            f.close()

        with open(f"{self.project.path}/patches/{patch.id}/metadata.json", "w") as f:
            f.write(json.dumps({
                "PatchGenerator": type(self).__name__
            }))
            f.close()
