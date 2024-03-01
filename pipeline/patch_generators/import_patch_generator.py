from pipeline.patch_generators.abstract.patch_generator import PatchGenerator
from pipeline.types.patch import Patch


class ImportPatchGenerator(PatchGenerator):
    def generate(self) -> Patch:
        # We always remove broken imports, we solve them at usage level
        return Patch()