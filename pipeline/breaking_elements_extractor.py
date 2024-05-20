import json
import os
import re
from typing import List

from pipeline.types.detected_fault import DetectedFault


class BreakingElementsExtractor:
    @staticmethod
    def extract(project_id: str, fault: DetectedFault) -> List[str]:
        data = BreakingElementsExtractor.get_dict()[project_id]
        if data is None:
            return []

        elements = data["allPotentialBreakingElements"] or []
        result = []
        for element in elements:
            found = re.search("([a-zA-Z0-9_.]+)\(.*?\)", element)
            if found is not None and found.group(1) is not None:
                result.append(found.group(1))

        additional_info = fault.error_info.additional_info
        found = re.search("symbol:   class ([a-zA-Z0-9_.]+)", additional_info)
        if found is not None and found.group(1) is not None:
            result.append(found.group(1))
            splitted = re.sub('([A-Z][a-z]+)', r' \1', re.sub('([A-Z]+)', r' \1', found.group(1))).split()
            for item in splitted:
                if len(item) > 3:
                    result.append(item)

        return result

    @staticmethod
    def get_dict() -> dict:
        bump_path = os.getenv("BUMP_PATH")
        with open(f"{bump_path}/repository/RQData/japicmp-results.json", "r") as f:
            return json.load(f)
