import json
import os
import subprocess
from typing import List

from pipeline.failure_extractor import FailureExtractor
from pipeline.patch_applicator import PatchApplicator
from pipeline.patch_generator import PatchGenerator
from pipeline.types.project import Project
from dotenv import load_dotenv

from pipeline.types.prompt import Prompt

load_dotenv()


class BenchmarkReport:
    def __init__(self, benchmark: str):
        self.benchmark = benchmark
        self.test_count = 0
        self.successful_test_count = 0

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


def main():
    benchmarks = {
        "bump": get_bump()
    }

    for projects in benchmarks.values():
        run_benchmark(projects)


def run_benchmark(projects: List[Project]):
    for project in projects:
        run_project(project)


def run_project(project: Project):
    extractor = FailureExtractor(project)
    failures = extractor.get_failures()
    failure = failures[0]
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


def get_bump() -> List[Project]:
    result = []
    bump_folder = os.getenv("BUMP_PATH")

    for filename in os.scandir(f"{bump_folder}/filtered_data"):
        if filename.is_file():
            key = filename.name.replace(".json", "")
            project = Project.from_bump(bump_folder, key)
            subprocess.run([
                'sh',
                'benchmarks/bump/scripts/clone_client_code.sh',
                project.project_id,
            ])
            result.append(project)

    return sorted(result, key=lambda x: x.project_id)


if __name__ == "__main__":
    main()
