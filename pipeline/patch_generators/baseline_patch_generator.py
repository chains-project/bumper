from pipeline.patch_generators.abstract.llm_patch_generator import LLMPatchGenerator
from pipeline.types.failure import Failure
from pipeline.types.project import Project
from pipeline.types.prompt import Prompt


class BaselinePatchGenerator(LLMPatchGenerator):
    def get_prompt(self) -> Prompt:
        return Prompt(
                template="base_prompt_template",
                values=self.get_params()
            )
    
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
