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
from pipeline.types.llm import LLMType
from pipeline.types.project import Project
from dotenv import load_dotenv
from pipeline.types.project_repair_status import ProjectRepairStatus
from pipeline.types.prompt import Prompt
load_dotenv()

class DummyFile(object):
  file = None
  def __init__(self, file):
    self.file = file

  def write(self, x):
    # Avoid print() second call (useless \n)
    if len(x.rstrip()) > 0:
        tqdm.write(x, file=self.file)

@contextlib.contextmanager
def nostdout():
    save_stdout = sys.stdout
    sys.stdout = DummyFile(sys.stdout)
    yield
    sys.stdout = save_stdout


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
            f.write(jsonpickle.encode(self.results, indent=4))
            f.close

    def add_result(self, key: str, result: ProjectRepairStatus):
        self.results[key] = result
        self.save()
        subprocess.call("git add . && git commit -m \"[Benchmark] update results\" && git push", shell=True)


def main(model: LLMType, pipeline: PipelineRunningMode, name: str):
    benchmarks = {
        "bump": get_bump()
    }

    for key in benchmarks.keys():
        run_benchmark(
            key=key,
            name=name,
            projects=benchmarks[key],
            pipeline=pipeline,
            model=model
        )


def run_benchmark(key: str, name: str, projects: List[Project], pipeline: PipelineRunningMode, model: LLMType):
    path = f"results/benchmark/{name}/{key}/{pipeline}/{model}"
    report = BenchmarkReport.load(from_path=f"{path}/report.json")

    progress = tqdm(projects, desc=f"Running projects for [{name}/{key}/{pipeline}/{model}]...", file=sys.stdout, miniters=1)
    for project in progress:
        with nostdout():
            try:
                if report.results.get(project.project_id) is None:
                    status = run_project(
                        project=project,
                        pipeline=pipeline,
                        model=model
                    )
                    save_patches(project=project, path=path)
                    report.add_result(key=project.project_id, result=status)
                else:
                    print(f"✅ {project.project_name} ({project.project_id})")
                    time.sleep(0.2)
            except KeyboardInterrupt:
                exit(1)
            except Exception as error:
                print(f"Skipping {project.project_id} because is failing to run:")
                print(error)

def save_patches(project: Project, path: str):
    os.makedirs(os.path.dirname(f"{path}/patches/"), exist_ok=True)
    subprocess.call(f"mv {project.path}/patches/* {path}/patches", shell=True)

def run_project(project: Project, pipeline: PipelineRunningMode, model: LLMType) -> ProjectRepairStatus:
    print(f"\n\n###### RUNNING PROJECT {project.project_name} ######")

    repairer = ProjectRepairer(project=project, pipeline=pipeline, model=model)
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
    parser.add_argument("-n", "--name", help="Name of the benchmark execution", type=str, required=True)
    parser.add_argument("-m", "--model", help="LLM Model", type=LLMType, choices=list(LLMType), required=True)
    parser.add_argument("-p", "--pipeline", help="Pipeline [STANDARD, BASELINE]", type=PipelineRunningMode, choices=list(PipelineRunningMode), required=True)

    options = parser.parse_args()
    main(
        name=options.name,
        pipeline=options.pipeline,
        model=options.model
    )