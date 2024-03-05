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
    def __init__(self, benchmark: str):
        self.benchmark = benchmark
        self.projects_count = 0
        self.successfull_repaired = 0

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
    
    def save(self, to_path: str):
        os.makedirs(os.path.dirname(to_path), exist_ok=True)
        with open(to_path, "w") as f:
            f.write(jsonpickle.encode(self))
            f.close


def main(mode: PipelineRunningMode):
    benchmarks = {
        "bump": get_bump()
    }

    for key in benchmarks.keys():
        run_benchmark(key, benchmarks[key], mode=mode)


def run_benchmark(key: str, projects: List[Project], mode: PipelineRunningMode):
    report = BenchmarkReport(benchmark=key)
    report.projects_count = len(projects)

    for project in tqdm(projects, desc=f"Running projects for {key}..."):
        status = run_project(project, mode=mode)
        if status.repaired:
            report.successfull_repaired += 1
    
    report.save(to_path=f"results/benchmark/{mode}/{key}.json")


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