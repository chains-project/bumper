from abc import ABC, abstractmethod
import json
import os

import jsonpickle

from pipeline.types.failure import Failure
from pipeline.types.llm import LLMType
from pipeline.types.patch import Patch
from pipeline.types.project import Project

class PatchGenerator(ABC):
    def __init__(self, failure: Failure, project: Project) -> None:
        super().__init__()
        self.failure = failure
        self.project = project
        self.after_init()

    def after_init(self):
        pass

    @abstractmethod
    def generate(self) -> Patch:
        pass
        
    def save_patch(self, patch: Patch):
        root_project = self.project.root_project or self.project
        path = f"{root_project.path}/patches/{patch.id}"
        os.makedirs(os.path.dirname(f"{path}/"), exist_ok=True)

        with open(f"{path}/patch.txt", "w") as f:
            f.write(patch.value)
            f.close()

        with open(f"{path}/original.txt", "w") as f:
            f.write(self.failure.detected_fault.method_code)
            f.close()

        with open(f"{path}/detected_fault.json", "w") as f:
            f.write(jsonpickle.encode(self.failure.detected_fault, indent=4))
            f.close()

        with open(f"{path}/api_diff.txt", "w") as f:
            f.write(self.failure.get_api_diff(only_relevant=False))
            f.close()

        with open(f"{path}/metadata.json", "w") as f:
            f.write(json.dumps({
                "PatchGenerator": type(self).__name__
            }))
            f.close()
