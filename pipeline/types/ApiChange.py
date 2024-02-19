from enum import Enum


class ApiChangeAction(Enum):
    ADD = "ADD"
    REMOVE = "REMOVE"


class ApiChange:
    def __init__(
            self,
            action: ApiChangeAction,
            value: str
    ):
        self.action = action
        self.value = value

    @staticmethod
    def from_json(data: dict):
        return ApiChange(
            action=ApiChangeAction(data["action"]),
            value=data["value"],
        )
