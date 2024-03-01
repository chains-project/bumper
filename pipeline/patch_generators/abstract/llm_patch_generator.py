from abc import abstractmethod
import os
import vertexai
from langchain_core.language_models import BaseLLM
from langchain_google_vertexai import VertexAI
from pipeline.patch_generators.abstract.patch_generator import PatchGenerator
from pipeline.types.failure import Failure

from pipeline.types.patch import Patch
from pipeline.types.project import Project
from pipeline.types.prompt import Prompt

class LLMPatchGenerator(PatchGenerator):
    def after_init(self):
        self.init_llm()
    
    def init_llm(self):
        vertexai.init(location=os.getenv("GOOGLE_CLOUD_REGION"))
        self.model = VertexAI(model_name="gemini-pro")

    def get_model(self) -> BaseLLM:
        return self.model

    def generate(self) -> Patch:
        md = self.get_model().invoke(self.get_prompt().get_text())
        result = Patch.from_md(md)

        return result
    
    def save_patch(self, patch: Patch):
        super().save_patch(patch)

        with open(f"{self.project.path}/patches/{patch.id}/prompt.txt", "w") as f:
            f.write(self.get_prompt().get_text())
            f.close()

    @abstractmethod
    def get_prompt() -> Prompt:
        pass