import re
import time


class Patch:
    id: int
    value: str
    force_validation: bool = False,
    __prompt: str = None
    __response: str = None

    def __init__(
            self,
            value="",
            force_validation=False,
            id=None
    ):
        self.value = value
        self.id = id or int(time.time_ns())
        self.force_validation = force_validation

    @staticmethod
    def from_md(md_text: str):
        found = re.search("```(?:java|Java)\s*[\r\n]+([\s\S]*?)[\r\n]*```", md_text)
        if found:
            return Patch(value=found.group(1) or "")
        else:
            return Patch(value="")
