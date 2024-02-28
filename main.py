import os
import subprocess

from pipeline.breaking_elements_extractor import BreakingElementsExtractor
from pipeline.failure_extractor import FailureExtractor
from pipeline.patch_applicator import PatchApplicator
from pipeline.patch_generator import PatchGenerator
from pipeline.project_repairer import ProjectRepairer
from pipeline.types.project import Project
from dotenv import load_dotenv

from pipeline.types.prompt import Prompt

load_dotenv()

project = Project.from_bump(
    bump_folder=os.getenv("BUMP_PATH"),
    project_id="1c0972fc3d905b9f2a305a78f8a158a0b3fd8639"
)

subprocess.run([
    'sh',
    'benchmarks/bump/scripts/clone_client_code.sh',
    project.project_id,
])

repairer = ProjectRepairer(project=project)
repairer.repair()
