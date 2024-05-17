import os
from pipeline.patch_generators.abstract.llm_patch_generator import LLMPatchGenerator
from pipeline.types.failure import Failure
from pipeline.types.llm import LLMType
from pipeline.types.project import Project
from pipeline.types.prompt import Prompt

"""
We use this generator also to find suitable replacement for the broken usage of the
dependency.
"""
class TypingPatchGenerator(LLMPatchGenerator):
    def __init__(self, failure: Failure, project: Project, model: LLMType, use_fully_qualified: bool = False) -> None:
        super().__init__(failure, project, model)
        self.use_fully_qualified = use_fully_qualified

    def get_prompt(self) -> Prompt:

        return Prompt(
                template=self.get_template(),
                values=self.get_params()
            )
    
    def get_template(self) -> str:
        if os.getenv("WITHOUT_APIDIFF") == "True":
            if self.use_fully_qualified is True:
                return "fully_qualified_typing_without_diff" 
            else:
                return "complete_instructions_on_top_without_diff"

        if self.use_fully_qualified is True:
            return "fully_qualified_typing"
        
        return "complete_instructions_on_top"
    
    def get_params(self) -> dict:
        failure = self.failure
        return {
            "qualified_in_class_code": failure.detected_fault.qualified_in_class_code,
            "in_class_client_code": failure.detected_fault.in_class_code,
            "qualified_client_code": failure.detected_fault.qualified_code,
            "client_code": failure.detected_fault.method_code,
            "error_message": failure.detected_fault.error_info.error_message,
            "additional_info": failure.detected_fault.error_info.additional_info,
            "bump_description": failure.get_api_diff(project_id=self.project.project_id)
        }
