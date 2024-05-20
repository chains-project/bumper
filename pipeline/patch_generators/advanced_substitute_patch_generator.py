import os
import re

from pipeline.patch_generators.abstract.llm_patch_generator import LLMPatchGenerator
from pipeline.patch_generators.typing_patch_generator import TypingPatchGenerator
from pipeline.types.failure import Failure
from pipeline.types.llm import LLMType
from pipeline.types.project import Project
from pipeline.types.prompt import Prompt

"""
We use this generator also to find suitable replacement for the broken usage of the
dependency.
"""
class AdvancedSubstitutePatchGenerator(TypingPatchGenerator):
    def get_params(self) -> dict:
        failure = self.failure
        api_diff = failure.get_api_diff(project_id=self.project.project_id)

        if len(api_diff) > 0:
            found = re.search("symbol:   class ([a-zA-Z0-9_.]+)", self.failure.detected_fault.error_info.additional_info)
            if found is not None and found.group(1) is not None:
                api_diff = self.enhance_api_diff(api_diff, old_element=found.group(1))

        return {
            "qualified_in_class_code": failure.detected_fault.qualified_in_class_code,
            "in_class_client_code": failure.detected_fault.in_class_code,
            "qualified_client_code": failure.detected_fault.qualified_code,
            "client_code": failure.detected_fault.method_code,
            "error_message": failure.detected_fault.error_info.error_message,
            "additional_info": failure.detected_fault.error_info.additional_info,
            "bump_description": api_diff
        }

    def enhance_api_diff(self, api_diff, old_element):
        prompt = Prompt(
            template="advance_api_diff_filter",
            values={
                "api_diff": api_diff,
                "old_element": old_element
            }
        )
        message = self.get_model().invoke(prompt.get_text())
        return message.content
