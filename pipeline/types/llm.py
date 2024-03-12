from enum import Enum
import os
from langchain_core.language_models import BaseLLM
from langchain_google_vertexai import VertexAI
from langchain_groq import ChatGroq
from langchain_openai import OpenAI

import vertexai


class LLMType(Enum):
    GEMINI = "gemini"
    GPT4 = "gtp4"
    LLAMA = "llama"
    MIXTRAL = "mixtral"

    def __str__(self):
        return self.value

    def get_model(self):
        return LLMResolver.get_model(self)

class LLMResolver:
    @staticmethod
    def get_model(for_type: LLMType) -> BaseLLM:
        definitions = {
            LLMType.GEMINI: LLMResolver.init_gemini,
            LLMType.GPT4: LLMResolver.init_gpt4,
            LLMType.LLAMA: LLMResolver.init_llama,
            LLMType.MIXTRAL: LLMResolver.init_mixtral
        }

        return (definitions[for_type]())
        

    @staticmethod
    def init_gemini() -> BaseLLM:
        vertexai.init(location=os.getenv("GOOGLE_CLOUD_REGION"))
        return VertexAI(
            model_name="gemini-pro",
            temperature=os.getenv("LLM_TEMPERATURE", 0.5),
            top_p=os.getenv("LLM_TOP_P", 1.0),
        )

    @staticmethod
    def init_gpt4() -> BaseLLM:
        return OpenAI(
            model_name="gpt-4",
            temperature=os.getenv("LLM_TEMPERATURE", 0.5),
            top_p=os.getenv("LLM_TOP_P", 1.0),
        )

    @staticmethod
    def init_llama() -> BaseLLM:
        return ChatGroq(
            model_name="llama2-70b-4096",
            temperature=os.getenv("LLM_TEMPERATURE", 0.5),
            top_p=os.getenv("LLM_TOP_P", 1.0),
        )
    
    @staticmethod
    def init_llama() -> BaseLLM:
        return ChatGroq(
            model_name="llama2-70b-4096",
            temperature=os.getenv("LLM_TEMPERATURE", 0.5),
            top_p=os.getenv("LLM_TOP_P", 1.0),
        )
    
    @staticmethod
    def init_mixtral() -> BaseLLM:
        return ChatGroq(
            model_name="mixtral-8x7b-32768",
            temperature=os.getenv("LLM_TEMPERATURE", 0.5),
            top_p=os.getenv("LLM_TOP_P", 1.0),
        )
