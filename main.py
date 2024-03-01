import os
import subprocess
import sys

from pipeline.breaking_elements_extractor import BreakingElementsExtractor
from pipeline.failure_extractor import FailureExtractor
from pipeline.patch_applicator import PatchApplicator
from pipeline.patch_generator_service import PatchGenerator
from pipeline.project_repairer import ProjectRepairer
from pipeline.types.project import Project
from dotenv import load_dotenv

from pipeline.types.prompt import Prompt

load_dotenv()


def main(project_id: str):
    project = Project.from_bump(
        bump_folder=os.getenv("BUMP_PATH"),
        project_id=project_id
    )

    subprocess.run([
        'sh',
        'benchmarks/bump/scripts/clone_client_code.sh',
        project.project_id,
    ])

    repairer = ProjectRepairer(project=project)
    repairer.repair()


if __name__ == "__main__":
    args = sys.argv
    if len(args) < 2:
        print("Need a project id!")
        exit(1)

    main(project_id=args[1])
