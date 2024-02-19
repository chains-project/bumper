from pipeline.failure_extractor import FailureExtractor
from pipeline.types.project import Project

project = Project(
    project_id="1ef97ea6c5b6e34151fe6167001b69e003449f95",
    project_name="flink-faker",
    library_name="datafaker",
    new_library_version="1.3.0",
    old_library_version="1.4.0",
    path="/Users/federicobono/Documents/IT/UNI/thesis/code/certa/benchmarks/bump/clients/1ef97ea6c5b6e34151fe6167001b69e003449f95"
)

extractor = FailureExtractor(project)

failures = extractor.get_failures()

print(f"identified {len(failures)} failure(s) in project {project.project_name}")
