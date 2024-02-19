class PromptGenerator:
    def __init__(self, template: str):
        self.template = template

    def get_text(self, values: dict):
        with open(self.get_template_path(), 'r') as file:
            data = file.read()
            for key in values.keys():
                data = data.replace("{{ " + key + " }}", values[key])
            return data

    def get_template_path(self):
        return f"prompts/templates/{self.template}.txt"
