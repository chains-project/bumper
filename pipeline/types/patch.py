import re


class Patch:
    value: str

    def __init__(
            self,
            value="",
    ):
        self.value = value

    @staticmethod
    def from_md(md_text: str):
        return Patch(
            value=re.search("```(?:java|Java)\s*[\r\n]+([\s\S]*?)[\r\n]*```", md_text).group(1)
        )
