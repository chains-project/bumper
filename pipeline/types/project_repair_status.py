from __future__ import annotations

class ProjectRepairStatus:
    def __init__(
            self,
            fixed_errors_count = 0,
            generated_patch_count = 0,
            repaired: bool = False,
    ) -> None:
        self.fixed_errors_count = fixed_errors_count
        self.generated_patch_count = generated_patch_count
        self.repaired = repaired

    def merge(self, status: ProjectRepairStatus) -> ProjectRepairStatus:
        self.generated_patch_count += status.generated_patch_count
        self.fixed_errors_count += status.fixed_errors_count
        self.repaired = True if self.repaired and status.repaired else False
        return self