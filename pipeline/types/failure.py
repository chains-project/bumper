from typing import List
from pipeline.types.api_change import ApiChange
from pipeline.types.detected_fault import DetectedFault


class Failure:
    def __init__(
            self,
            api_changes: List[ApiChange],
            detected_fault: DetectedFault
    ):
        self.detected_fault = detected_fault
        self.api_changes = api_changes

    @staticmethod
    def from_json(data: dict):
        return Failure(
            api_changes=[ApiChange.from_json(x) for x in data['apiChanges']],
            detected_fault=DetectedFault.from_json(data['detectedFault'])
        )

    def get_api_diff(self):
        plausible_changes = filter(
            lambda x: self.detected_fault.plausible_dependency_identifier in x.value,
            self.api_changes
        )
        return "\n".join([c.get_diff() for c in plausible_changes])
