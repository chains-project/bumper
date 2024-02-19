class Project:
    def __init__(
            self,
            project_id: str,
            project_name: str,
            path: str,
            library_name: str,
            old_library_version: str,
            new_library_version: str
    ) -> None:
        self.project_name = project_name
        self.project_id = project_id
        self.path = path
        self.library_name = library_name
        self.old_library_version = old_library_version
        self.new_library_version = new_library_version
