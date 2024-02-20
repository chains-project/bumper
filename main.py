import subprocess

from pipeline.failure_extractor import FailureExtractor
from pipeline.patch_applicator import PatchApplicator
from pipeline.patch_generator import PatchGenerator
from pipeline.types.project import Project
from dotenv import load_dotenv

from pipeline.types.prompt import Prompt

load_dotenv()

# project = Project(
#     project_id="1ef97ea6c5b6e34151fe6167001b69e003449f95",
#     project_name="flink-faker",
#     library_name="datafaker",
#     library_group_id="net.datafaker",
#     new_library_version="1.4.0",
#     old_library_version="1.3.0",
#     path="/Users/federicobono/Documents/IT/UNI/thesis/code/certa/benchmarks/bump/clients/1ef97ea6c5b6e34151fe6167001b69e003449f95",
# )

# project = Project(
#     project_id="5fcd0c3ad7727850c47602b17530dc355e5bd097",
#     project_name="pitest-mutation-testing-elements-plugin",
#     library_name="pitest-entry",
#     library_group_id="org.pitest",
#     new_library_version="1.10.0",
#     old_library_version="1.9.11",
#     path="/Users/federicobono/Documents/IT/UNI/thesis/code/certa/benchmarks/bump/clients/5fcd0c3ad7727850c47602b17530dc355e5bd097"
# )

project = Project(
    project_id="0abf7148300f40a1da0538ab060552bca4a2f1d8",
    project_name="biapi",
    library_name="jasperreports",
    library_group_id="net.sf.jasperreports",
    new_library_version="6.18.1",
    old_library_version="6.19.1",
    path="/Users/federicobono/Documents/IT/UNI/thesis/code/certa/benchmarks/bump/clients/0abf7148300f40a1da0538ab060552bca4a2f1d8"
)

subprocess.run([
    'sh',
    'benchmarks/bump/scripts/clone_client_code.sh',
    project.project_id,
])

extractor = FailureExtractor(project)
failures = extractor.get_failures()
failure = failures[0]
# template = "base_prompt_template"
prompt = Prompt(
    template="with_class_code_prompt_template_with_library_specs",
    values={
        "in_class_client_code": failure.detected_fault.in_class_code,
        "client_code": failure.detected_fault.method_code,
        "error_message": failure.detected_fault.error_info.error_message,
        "bump_description": failure.get_api_diff()
    }
)

patch_generator = PatchGenerator()
print(f"Generating patch for project {project.project_name}")

patch = patch_generator.generate(prompt)
project.save_patch(patch, prompt=prompt)

patch_applicator = PatchApplicator(project)
patch_applicator.save_patched_code(patch, failure)
print("File patched")
print("Checking for validity...")
subprocess.run([
    'sh',
    'benchmarks/bump/scripts/test_patched_code.sh',
    project.project_id,
    patch_applicator.get_patched_code_path(patch, failure)
])
