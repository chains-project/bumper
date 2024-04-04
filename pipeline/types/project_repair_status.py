from __future__ import annotations


class ProjectRepairStatus:
    def __init__(
            self,
            fixed_errors_count=0,
            generated_patch_count=0,
            patches=[],
            repaired: bool = False,
            initial_errors_count=0,
    ) -> None:
        self.initial_errors_count = initial_errors_count
        self.fixed_errors_count = fixed_errors_count
        self.generated_patch_count = generated_patch_count
        self.repaired = repaired
        self.patches = patches

    def merge(self, status: ProjectRepairStatus) -> ProjectRepairStatus:
        self.generated_patch_count += status.generated_patch_count
        self.fixed_errors_count += status.fixed_errors_count
        self.patches = self.patches + status.patches
        self.repaired = True if self.repaired and status.repaired else False
        return self
