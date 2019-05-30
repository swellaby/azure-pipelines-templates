from test.test_utilities import parse_any_template_yaml_file

template = "artifacts/download/specific-pipeline-latest-artifact.yml"
contents = parse_any_template_yaml_file(template)
steps = contents["steps"]
parameters = contents["parameters"]
step = steps[0]
inputs = step["inputs"]


def test_num_steps():
    assert len(steps) == 1


def test_project_parameter_default():
    assert parameters["project"] == "OpenSource"


def test_pipeline_parameter_default():
    assert parameters["pipeline"] == ""


def test_specific_build_with_triggering_parameter_default():
    assert parameters["specificBuildWithTriggering"] is False


def test_artifact_name_parameter_default():
    assert parameters["artifactName"] == ""


def test_branch_name_parameter_default():
    assert parameters["branchName"] == ""


def test_item_pattern_parameter_default():
    assert parameters["itemPattern"] == ""


def test_tags_parameter_default():
    assert parameters["tags"] == ""


def test_target_path_parameter_default():
    assert parameters["targetPath"] == ""


def test_task_display_name_parameter_default():
    assert parameters["taskDisplayName"] == "Download pipeline artifact"


def test_step_type():
    assert step["task"] == "DownloadPipelineArtifact@1"


def test_step_display_name():
    assert step["displayName"] == "${{ parameters.taskDisplayName }}"


def test_step_build_type_input():
    assert inputs["buildType"] == "specific"


def test_step_project_input():
    assert inputs["project"] == "${{ parameters.project }}"


def test_step_pipeline_input():
    assert inputs["pipeline"] == "${{ parameters.pipeline }}"


def test_step_specific_build_with_triggering_input():
    value = inputs["specificBuildWithTriggering"]
    assert value == "${{ parameters.specificBuildWithTriggering }}"


def test_step_artifact_name_input():
    assert inputs["artifactName"] == "${{ parameters.artifactName }}"


def test_step_branch_name_input():
    assert inputs["branchName"] == "${{ parameters.branchName }}"


def test_step_item_pattern_input():
    assert inputs["itemPattern"] == "${{ parameters.itemPattern }}"


def test_step_tags_input():
    assert inputs["tags"] == "${{ parameters.tags }}"


def test_step_target_path_input():
    assert inputs["targetPath"] == "${{ parameters.targetPath }}"
