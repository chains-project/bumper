from pipeline.patch_generators.abstract.patch_generator import PatchGenerator
from pipeline.types.patch import Patch

"""
For decorators we typically get the "does not override" error
so fix is simply always removing the @Override decorator.
 
Class is defined so that we can easily add other decorators to manage
"""
class DecoratorPatchGenerator(PatchGenerator):
    def generate(self) -> Patch:
        client_code = self.failure.detected_fault.method_code

        return Patch(
            value=client_code.replace(self.get_decorator(), "")
        )
    
    def get_decorator(self) -> str:
        message = self.failure.detected_fault.error_info.error_message

        if "override" in message:
            return "@Override"
        else:
            return ""