from abc import abstractmethod
import os
import vertexai
from langchain_core.language_models import BaseChatModel
from pipeline.patch_generators.abstract.patch_generator import PatchGenerator
from pipeline.types.failure import Failure
from pipeline.types.llm import LLMType

from pipeline.types.patch import Patch
from pipeline.types.project import Project
from pipeline.types.prompt import Prompt

class LLMPatchGenerator(PatchGenerator):
    def __init__(self, failure: Failure, project: Project, model: LLMType) -> None:
        self.llm_type = model
        super().__init__(failure, project)

    def after_init(self):
        self.init_llm()
    
    def init_llm(self):
        self.model = self.llm_type.get_model()

    def get_model(self) -> BaseChatModel:
        return self.model

    def generate(self) -> Patch:
        message = self.get_model().invoke(self.get_prompt().get_text())
        md = message.content
        result = Patch.from_md(md)

        with open(f"{self.project.path}/patches/{result.id}/model_response.md", "w") as f:
            f.write(md)
            f.close()

        return result
    
    def save_patch(self, patch: Patch):
        super().save_patch(patch)

        with open(f"{self.project.path}/patches/{patch.id}/prompt.txt", "w") as f:
            f.write(self.get_prompt().get_text())
            f.close()

    @abstractmethod
    def get_prompt() -> Prompt:
        pass