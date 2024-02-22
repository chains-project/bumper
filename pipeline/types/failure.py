from typing import List

from pipeline.breaking_elements_extractor import BreakingElementsExtractor
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

    def get_api_diff(self, project_id: str, only_relevant: bool = True) -> str:
        if not only_relevant:
            return "\n".join([c.get_diff() for c in self.api_changes])

        plausible_changes = filter(
            lambda x: any(
                element in x.value for element in BreakingElementsExtractor.extract(project_id)
            ),
            self.api_changes
        )
        return "\n".join([c.get_diff() for c in plausible_changes])
