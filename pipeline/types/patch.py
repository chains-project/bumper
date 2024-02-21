import re
import time


class Patch:
    id: int
    value: str

    def __init__(
            self,
            value="",
    ):
        self.value = value
        self.id = int(time.time())

    @staticmethod
    def from_md(md_text: str):
        found = re.search("```(?:java|Java)\s*[\r\n]+([\s\S]*?)[\r\n]*```", md_text)
        if found:
            return Patch(value=found.group(1) or "")
        else:
            return Patch(value="")
