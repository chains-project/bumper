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
        return Patch(
            value=re.search("```(?:java|Java)\s*[\r\n]+([\s\S]*?)[\r\n]*```", md_text).group(1)
        )
