from typing import List
from pipeline.types.ApiChange import ApiChange
from pipeline.types.DetectedFault import DetectedFault

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
