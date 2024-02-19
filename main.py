from pipeline.failure_extractor import FailureExtractor
from pipeline.prompt_generator import PromptGenerator
from pipeline.types.project import Project

project = Project(
    project_id="1ef97ea6c5b6e34151fe6167001b69e003449f95",
    project_name="flink-faker",
    library_name="datafaker",
    library_group_id="net.datafaker",
    new_library_version="1.4.0",
    old_library_version="1.3.0",
    path="/Users/federicobono/Documents/IT/UNI/thesis/code/certa/benchmarks/bump/clients/1ef97ea6c5b6e34151fe6167001b69e003449f95",
)

extractor = FailureExtractor(project)

failures = extractor.get_failures()

failure = failures[0]
template = "base_prompt_template"
generator = PromptGenerator(template)
params = {
    "client_code": failure.detected_fault.method_code,
    "error_message": failure.detected_fault.error_info.error_message,
    "bump_description": failure.get_api_diff()
}
print(generator.get_text(params))
