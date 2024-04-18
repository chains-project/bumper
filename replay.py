import argparse
import contextlib
import json
import os
import subprocess
import sys
import time
from typing import List

import jsonpickle
from tqdm import tqdm

from pipeline.failure_extractor import FailureExtractor
from pipeline.patch_applicator import PatchApplicator
from pipeline.patch_generator_service import PatchGenerator, PipelineRunningMode
from pipeline.project_repairer import ProjectRepairer
from pipeline.types.detected_fault import DetectedFault
from pipeline.types.failure import Failure
from pipeline.types.llm import LLMType
from pipeline.types.patch import Patch
from pipeline.types.project import Project
from dotenv import load_dotenv
from pipeline.types.project_repair_status import ProjectRepairStatus
from benchmark import BenchmarkReport

def main(model: LLMType, pipeline: PipelineRunningMode, name: str, benchmark: str, project_id: str):
    bump_folder = os.getenv("BUMP_PATH")
    path = f"results/benchmark/{name}/{benchmark}/{pipeline}/{model}"
    report = BenchmarkReport.load(from_path=f"{path}/report.json")
    if report.results.get(project_id) is None:
        print(f"Cannot find execution report for project {project_id}")
        exit(1)

    project = Project.from_bump(bump_folder, project_id)
    project_report = report.results.get(project_id)

    # Clean up
    subprocess.run([
        'bash',
        'benchmarks/bump/scripts/clone_client_code.sh',
        project.project_id,
    ])
    subprocess.call(f"rm -rf {project.path}/patches", shell=True)
    subprocess.call(f"rm -rf {project.path}/patched_code", shell=True)

    original_project_path = project.path

    for id in project_report.patches:
        patch_path = f"{path}/{project_id}/patches/{id}"
        if not os.path.exists(patch_path):
            print(f"{patch_path} does not exist!")
            exit(1)

        with open(f"{patch_path}/patch.txt", "r") as f:
            patch_content = f.read()
            f.close()

        with open(f"{patch_path}/detected_fault.json", "r") as f:
            fault = jsonpickle.decode(f.read())
            failure = Failure(api_changes=[], detected_fault=fault)
            f.close()

        patch = Patch(id=id, value=patch_content)
        patch_applicator = PatchApplicator(project)
        patch_applicator.save_patched_code(patch, failure)
        project.path = f"{project.path}/patched_code/{id}"
    
    # project.path = original_project_path

    print("Running final version")
    try:
        result = subprocess.run([
            'bash',
            'benchmarks/bump/scripts/test_patched_code.sh',
            project.project_id,
            f"{project.path}/{project.project_name}",
        ], timeout=300, stdout=subprocess.PIPE)
        print (f"Result: {result}")
    except subprocess.TimeoutExpired:
        print("[ERROR] test_patched_code.sh timed out! Cleaning up before continuing...")
        subprocess.run([
            'bash',
            'benchmarks/bump/scripts/cleanup_after_failure.sh',
            project.project_id,
        ], stdout=subprocess.PIPE)    
    
    print(f"Final version path: {project.path}")

if __name__ == "__main__":
    load_dotenv(override=True)

    parser = argparse.ArgumentParser()
    parser.add_argument("-k", "--project", help="ID of the project", type=str, required=True)
    parser.add_argument("-b", "--benchmark", help="Name of the benchmark", type=str, default="bump")
    parser.add_argument("-n", "--name", help="Name of the benchmark execution", type=str, required=True)
    parser.add_argument("-m", "--model", help="LLM Model", type=LLMType, choices=list(LLMType), required=True)
    parser.add_argument("-p", "--pipeline", help="Pipeline [STANDARD, BASELINE]", type=PipelineRunningMode,
                        choices=list(PipelineRunningMode), required=True)

    options = parser.parse_args()
    main(
        name=options.name,
        pipeline=options.pipeline,
        model=options.model,
        benchmark=options.benchmark or "bump",
        project_id=options.project
    )
