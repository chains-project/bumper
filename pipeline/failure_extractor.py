import json
import subprocess
from typing import List

from pipeline.types.failure import Failure
from pipeline.types.project import Project


class FailureExtractor:
    def __init__(self, project: Project):
        self.project = project

    def get_failures(self) -> List[Failure]:
        log_path = f"{self.project.path}/{self.project.project_name}/{self.project.project_id}.log"

        old_dependency = f"{self.project.library_name}-{self.project.old_library_version}"
        new_dependency = f"{self.project.library_name}-{self.project.new_library_version}"

        old_dependency_path = f"{self.project.path}/{old_dependency}.jar"
        new_dependency_path = f"{self.project.path}/{new_dependency}.jar"

        result = subprocess.run([
            'java',
            '-jar', 'libs/java/target/Explaining.jar',
            '-c', self.project.path,
            '-o', old_dependency_path,
            '-n', new_dependency_path,
            '-l', log_path
        ], stdout=subprocess.PIPE)
        json_data = json.loads(result.stdout)

        return [Failure.from_json(row) for row in json_data]