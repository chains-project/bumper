class Prompt:
    def __init__(
            self,
            template: str,
            values: dict
    ):
        self.template = template
        self.values = values

    def get_text(self, values: dict = None):
        values = values or self.values

        with open(self.get_template_path(), 'r') as file:
            data = file.read()
            for key in values.keys():
                data = data.replace("{{ " + key + " }}", values.get(key) or "")
            return data

    def get_template_path(self):
        return f"prompts/templates/{self.template}.txt"
