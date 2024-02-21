import json
import os
import re
from typing import List


class BreakingElementsExtractor:
    @staticmethod
    def extract(project_id: str) -> List[str]:
        data = BreakingElementsExtractor.get_dict()[project_id]
        if data is None:
            return []

        elements = data["allPotentialBreakingElements"] or []
        result = []
        for element in elements:
            found = re.search("([a-zA-Z0-9_.]+)\(.*?\)", element)
            if found is not None and found.group(1) is not None:
                result.append(found.group(1))

        return result

    @staticmethod
    def get_dict() -> dict:
        bump_path = os.getenv("BUMP_PATH")
        with open(f"{bump_path}/repository/RQData/japicmp-results.json", "r") as f:
            return json.load(f)
