from pipeline.types.error_info import ErrorInfo


class DetectedFault:
    def __init__(
            self,
            identifier: int,
            method_name: str,
            method_code: str,
            qualified_code: str,
            in_class_code: str,
            qualified_in_class_code: str,
            client_line_number: int,
            client_end_line_number: int,
            error_info: ErrorInfo,
            plausible_dependency_identifier: str
    ):
        self.identifier = identifier
        self.in_class_code = in_class_code
        self.qualified_in_class_code = qualified_in_class_code
        self.plausible_dependency_identifier = plausible_dependency_identifier
        self.error_info = error_info
        self.client_end_line_number = client_end_line_number
        self.client_line_number = client_line_number
        self.method_code = method_code
        self.qualified_code = qualified_code
        self.method_name = method_name

    @staticmethod
    def from_json(data: dict):
        return DetectedFault(
            identifier=data['identifier'],
            method_name=data['methodName'],
            method_code=data['methodCode'],
            qualified_code=data['qualifiedMethodCode'] or data["methodCode"],
            client_line_number=data['clientLineNumber'],
            client_end_line_number=data['clientEndLineNumber'],
            plausible_dependency_identifier=data['plausibleDependencyIdentifier'],
            error_info=ErrorInfo.from_json(data['errorInfo']),
            in_class_code=data['inClassCode'],
            qualified_in_class_code=data['qualifiedInClassCode'],
        )
