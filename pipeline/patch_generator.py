import os
import vertexai
from langchain_core.language_models import BaseLLM
from langchain_google_vertexai import VertexAI

from pipeline.types.patch import Patch
from pipeline.types.prompt import Prompt


class PatchGenerator:
    def __init__(self):
        self.model = None
        self.init_llm()

    def init_llm(self):
        vertexai.init(location=os.getenv("GOOGLE_CLOUD_REGION"))
        self.model = VertexAI(model_name="gemini-pro")

    def get_model(self) -> BaseLLM:
        return self.model

    def generate(self, prompt: Prompt) -> Patch:
        md = self.get_model().invoke(prompt.get_text())
        result = Patch.from_md(md)

        return result
