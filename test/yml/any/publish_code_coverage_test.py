from test.test_utilities import parse_any_template_yaml_file

contents = parse_any_template_yaml_file("publish-code-coverage.yml")
steps = contents["steps"]
parameters = contents["parameters"]
step = steps[0]
inputs = step["inputs"]


def test_num_steps():
    assert len(steps) == 1


def test_code_coverage_tool_parameter_default():
    assert parameters["codeCoverageTool"] == "Cobertura"


def test_summary_file_location_parameter_default():
    value = parameters["summaryFileLocation"]
    exp = "$(Build.SourcesDirectory)/.coverage/unit/cobertura-coverage.xml"
    assert value == exp


def test_report_directory_parameter_default():
    value = parameters["reportDirectory"]
    assert value == "$(Build.SourcesDirectory)/.coverage/unit"


def test_run_title_parameter_default():
    assert parameters["additionalCodeCoverageFiles"] == ""


def test_fail_if_coverage_empty_parameter_default():
    assert parameters["failIfCoverageEmpty"] is False


def test_task_display_name_parameter_default():
    assert parameters["taskDisplayName"] == "Publish coverage results"


def test_step_type():
    assert step["task"] == "PublishCodeCoverageResults@1"


def test_step_display_name():
    assert step["displayName"] == "${{ parameters.taskDisplayName }}"


def test_step_code_coverage_tool_input():
    assert inputs["codeCoverageTool"] == "${{ parameters.codeCoverageTool }}"


def test_step_summary_file_location_input():
    value = "${{ parameters.summaryFileLocation }}"
    assert inputs["summaryFileLocation"] == value


def test_step_report_directory_input():
    value = inputs["reportDirectory"]
    assert value == "${{ parameters.reportDirectory }}"


def test_step_additional_code_coverage_files_input():
    value = inputs["additionalCodeCoverageFiles"]
    assert value == "${{ parameters.additionalCodeCoverageFiles }}"


def test_step_fail_if_coverage_empty_input():
    value = inputs["failIfCoverageEmpty"]
    assert value == "${{ parameters.failIfCoverageEmpty }}"
