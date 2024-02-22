import os
import subprocess

from pipeline.breaking_elements_extractor import BreakingElementsExtractor
from pipeline.failure_extractor import FailureExtractor
from pipeline.patch_applicator import PatchApplicator
from pipeline.patch_generator import PatchGenerator
from pipeline.types.project import Project
from dotenv import load_dotenv

from pipeline.types.prompt import Prompt

load_dotenv()

project = Project.from_bump(
    bump_folder=os.getenv("BUMP_PATH"),
    project_id="9836e07e553e29f16ee35b5d7e4d0370e1789ecd"
)

subprocess.run([
    'sh',
    'benchmarks/bump/scripts/clone_client_code.sh',
    project.project_id,
])


extractor = FailureExtractor(project)
failures = extractor.get_failures()
failure = failures[0]
api_dff = failure.get_api_diff(project.project_id)

if api_dff == "":
    relevant_keys = '\n'.join(BreakingElementsExtractor.extract(project.project_id))
    print("ERROR: Cannot find any relevant api-diff. It is probable better to manually fix this breaking update.")
    print(f"All diffs: {failure.get_api_diff(project.project_id, False)}")
    print(f"Relevant keys: {relevant_keys}")
    # exit(1)

# print(failure.get_api_diff(project.project_id))
# exit(0)

prompt = Prompt(
    template="complete_instructions_on_top",
    values={
        "in_class_client_code": failure.detected_fault.in_class_code,
        "client_code": failure.detected_fault.method_code,
        "error_message": failure.detected_fault.error_info.error_message,
        "bump_description": failure.get_api_diff(project_id=project.project_id)
    }
)
patch_generator = PatchGenerator()
print(f"Generating patch for project {project.project_name}")
patch = patch_generator.generate(prompt)
project.save_patch(patch, prompt=prompt, failure=failure)
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
