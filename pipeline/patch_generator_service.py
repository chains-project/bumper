import os
import vertexai
from langchain_core.language_models import BaseLLM
from langchain_google_vertexai import VertexAI
from pipeline.patch_generators.abstract.patch_generator import PatchGenerator
from pipeline.patch_generators.decorator_patch_generator import DecoratorPatchGenerator
from pipeline.patch_generators.import_patch_generator import ImportPatchGenerator
from pipeline.patch_generators.typing_patch_generator import TypingPatchGenerator
from pipeline.types.failure import Failure

from pipeline.types.project import Project

class PatchGeneratorService:
    
    @staticmethod
    def get_generator(failure: Failure, project: Project) -> PatchGenerator:
        error_message = failure.detected_fault.error_info.error_message

        if "method does not override" in error_message:
            return DecoratorPatchGenerator(failure=failure, project=project)
        
        if "incompatible types" in error_message:
            return TypingPatchGenerator(failure=failure, project=project)
        
        if "reference to" in error_message and "is ambiguous" in error_message:
            return TypingPatchGenerator(failure=failure, project=project)
        
        if "cannot find symbol" in error_message:
            if PatchGeneratorService.is_import_error(failure=failure):
                return ImportPatchGenerator(failure=failure, project=project)
            
            # TODO: make substitute patch generator
            return TypingPatchGenerator(failure=failure, project=project)

    @staticmethod
    def is_import_error(failure: Failure) -> bool:
        if "import" not in failure.detected_fault.method_code:
            return False
        
        if failure.detected_fault.client_end_line_number - failure.detected_fault.client_line_number > 0:
            return False
        
        return True