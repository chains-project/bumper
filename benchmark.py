import argparse
import contextlib
import json
import os
import subprocess
import sys
from typing import List

import jsonpickle
from tqdm import tqdm

from pipeline.failure_extractor import FailureExtractor
from pipeline.patch_applicator import PatchApplicator
from pipeline.patch_generator_service import PatchGenerator, PipelineRunningMode
from pipeline.project_repairer import ProjectRepairer
from pipeline.types.project import Project
from dotenv import load_dotenv
from pipeline.types.project_repair_status import ProjectRepairStatus
from pipeline.types.prompt import Prompt
load_dotenv()


class BenchmarkReport:
    def __init__(self, path: str):
        self.path = path
        self.results = {}

    @staticmethod
    def load(from_path: str):
        report = BenchmarkReport(path=from_path)
        if os.path.exists(from_path):
            with open(from_path, "r") as f:
                report.results = jsonpickle.decode(f.read())
                f.close()
        return report
            

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def save(self):
        to_path = self.path
        os.makedirs(os.path.dirname(to_path), exist_ok=True)
        with open(to_path, "w") as f:
            f.write(jsonpickle.encode(self.results))
            f.close

    def add_result(self, key: str, result: ProjectRepairStatus):
        self.results[key] = result
        self.save()


def main(mode: PipelineRunningMode):
    benchmarks = {
        "bump": get_bump()
    }

    for key in benchmarks.keys():
        run_benchmark(key, benchmarks[key], mode=mode)


def run_benchmark(key: str, projects: List[Project], mode: PipelineRunningMode):
    path = f"results/benchmark/{mode}/{key}.json"
    report = BenchmarkReport.load(from_path=path)

    for project in tqdm(projects, desc=f"Running projects for {key}..."):
        try:
            if report.results.get(project.project_id) is not None:
                print(f"Skipping {project.project_id} because already run.")
                continue
            status = run_project(project, mode=mode)
            report.add_result(key=project.project_id, result=status)
        except:
            print(f"Skipping {project.project_id} because is failing to run.")


def run_project(project: Project, mode: PipelineRunningMode) -> ProjectRepairStatus:
    subprocess.run([
        'sh',
        'benchmarks/bump/scripts/clone_client_code.sh',
        project.project_id,
    ])

    repairer = ProjectRepairer(project=project, mode=mode)
    return repairer.repair()


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
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--mode", help="Mode [STANDARD, BASELINE]", type=PipelineRunningMode, choices=list(PipelineRunningMode), required=True)

    options = parser.parse_args()
    main(
        mode=options.mode
    )