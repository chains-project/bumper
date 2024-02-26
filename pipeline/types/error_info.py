class ErrorInfo:
    def __init__(
            self,
            client_line_position: str,
            client_file_path: str,
            error_message: str,
            additional_info: str
    ):
        self.additional_info = additional_info
        self.error_message = error_message
        self.client_file_path = client_file_path
        self.client_line_position = client_line_position

    @staticmethod
    def from_json(data: dict):
        return ErrorInfo(
            client_line_position=data["clientLinePosition"],
            client_file_path=data["clientFilePath"],
            error_message=data["errorMessage"],
            additional_info=data["additionalInfo"],
        )
