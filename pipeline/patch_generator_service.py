from enum import Enum
import os
import vertexai
from langchain_core.language_models import BaseLLM
from langchain_google_vertexai import VertexAI
from pipeline.patch_generators.abstract.patch_generator import PatchGenerator
from pipeline.patch_generators.baseline_patch_generator import BaselinePatchGenerator
from pipeline.patch_generators.decorator_patch_generator import DecoratorPatchGenerator
from pipeline.patch_generators.import_patch_generator import ImportPatchGenerator
from pipeline.patch_generators.typing_patch_generator import TypingPatchGenerator
from pipeline.types.failure import Failure
from pipeline.types.llm import LLMType

from pipeline.types.project import Project

class PipelineRunningMode(Enum):
    BASELINE = "baseline"
    STANDARD = "standard"

    def __str__(self):
        return self.value

class PatchGeneratorService:
    
    @staticmethod
    def get_generator(failure: Failure, project: Project, pipeline: PipelineRunningMode = PipelineRunningMode.STANDARD, model: LLMType = LLMType.GEMINI) -> PatchGenerator:
        if pipeline is PipelineRunningMode.BASELINE:
            return BaselinePatchGenerator(failure=failure, project=project, model=model)

        error_message = failure.detected_fault.error_info.error_message

        if "method does not override" in error_message:
            return DecoratorPatchGenerator(failure=failure, project=project)
        
        if "incompatible types" in error_message:
            return TypingPatchGenerator(failure=failure, project=project, model=model)
        
        if "reference to" in error_message and "is ambiguous" in error_message:
            return TypingPatchGenerator(failure=failure, project=project, model=model)
        
        if "cannot find symbol" in error_message:
            if PatchGeneratorService.is_import_error(failure=failure):
                return ImportPatchGenerator(failure=failure, project=project)
            
            # TODO: make substitute patch generator
            return TypingPatchGenerator(failure=failure, project=project, use_fully_qualified=True, model=model)
        
        print(f"PatchGenerator not found for {error_message}")
        exit(1)

    @staticmethod
    def is_import_error(failure: Failure) -> bool:
        if "import" not in failure.detected_fault.method_code:
            return False
        
        if failure.detected_fault.client_end_line_number - failure.detected_fault.client_line_number > 0:
            return False
        
        return True