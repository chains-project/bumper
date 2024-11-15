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
        prompt = self.get_prompt().get_text()
        message = self.get_model().invoke(prompt)
        md = message.content
        patch = Patch.from_md(md)
        
        patch.__prompt = prompt
        patch.__response = md

        return patch
    
    def save_patch(self, patch: Patch):
        super().save_patch(patch)

        root_project = self.project.root_project or self.project
        path = f"{root_project.path}/patches/{patch.id}"

        with open(f"{path}/prompt.txt", "w") as f:
            f.write(patch.__prompt)
            f.close()

        with open(f"{path}/model_response.md", "w") as f:
            f.write(patch.__response)
            f.close()

    @abstractmethod
    def get_prompt(self) -> Prompt:
        pass