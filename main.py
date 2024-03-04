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
    result = project.get_result()

    if result["repaired"] is True:
        print(f"PROJECT {project.project_id} IS ALREADY REPAIRED!")
        exit(0)

    subprocess.run([
        'sh',
        'benchmarks/bump/scripts/clone_client_code.sh',
        project.project_id,
    ])

    repairer = ProjectRepairer(project=project)
    if repairer.repair():
        print(f"PROJECT {project.project_id} REPAIRED!")
        project.set_as_repaired()
        exit(0)
    else:
        print(f"FAILED TO REPAIR PROJECT {project.project_id}")
        exit(1)


if __name__ == "__main__":
    args = sys.argv
    if len(args) < 2:
        print("Need a project id!")
        exit(1)

    main(project_id=args[1])
