from pipeline.patch_generators.abstract.llm_patch_generator import LLMPatchGenerator
from pipeline.types.prompt import Prompt


class TypingPatchGenerator(LLMPatchGenerator):
    def get_prompt(self) -> Prompt:
        failure = self.failure

        return Prompt(
                template="complete_instructions_on_top",
                values={
                    "in_class_client_code": failure.detected_fault.in_class_code,
                    "client_code": failure.detected_fault.method_code,
                    "error_message": failure.detected_fault.error_info.error_message,
                    "additional_info": failure.detected_fault.error_info.additional_info,
                    "bump_description": failure.get_api_diff(project_id=self.project.project_id)
                }
            )