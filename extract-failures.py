import json
import subprocess

from pipeline.types.Failure import Failure

client_id = "5fcd0c3ad7727850c47602b17530dc355e5bd097"
project_folder = "pitest-mutation-testing-elements-plugin"
project_path = f"/Users/federicobono/Documents/IT/UNI/thesis/code/breaking-good/clients/{client_id}"
log_path = f"{project_path}/{project_folder}/{client_id}.log"

old_dependency = "pitest-entry-1.9.11"
new_dependency = "pitest-entry-1.10.0"

old_dependency_path = f"{project_path}/{old_dependency}.jar"
new_dependency_path = f"{project_path}/{new_dependency}.jar"

result = subprocess.run([
    'java',
    '-jar', 'libs/java/target/Explaining.jar',
    '-c', project_path,
    '-o', old_dependency_path,
    '-n', new_dependency_path,
    '-l', log_path
], stdout=subprocess.PIPE)
json_data = json.loads(result.stdout)

failures = [Failure.from_json(row) for row in json_data]

print(failures[0].detected_fault.method_code)
