from test.test_utilities import parse_any_template_yaml_file

contents = parse_any_template_yaml_file("publish-test-results.yml")
steps = contents["steps"]
parameters = contents["parameters"]
step = steps[0]
inputs = step["inputs"]


def test_num_steps():
    assert len(steps) == 1


def test_results_format_parameter_default():
    assert parameters["testResultsFormat"] == "JUnit"


def test_results_files_parameter_default():
    assert parameters["testResultsFiles"] == "junit.xml"


def test_search_folder_parameter_default():
    value = parameters["searchFolder"]
    assert value == "$(Build.SourcesDirectory)/.testresults/unit"


def test_run_title_parameter_default():
    value = parameters["testRunTitle"]
    assert value == "Unit Tests::Build $(Build.BuildId)"


def test_task_display_name_parameter_default():
    assert parameters["taskDisplayName"] == "Publish unit test results"


def test_step_type():
    assert step["task"] == "PublishTestResults@2"


def test_step_display_name():
    assert step["displayName"] == "${{ parameters.taskDisplayName }}"


def test_step_results_format_input():
    assert inputs["testResultsFormat"] == "${{ parameters.testResultsFormat }}"


def test_step_results_files_input():
    assert inputs["testResultsFiles"] == "${{ parameters.testResultsFiles }}"


def test_step_search_folder_input():
    value = inputs["searchFolder"]
    assert value == "${{ parameters.searchFolder }}"


def test_step_run_title_input():
    value = inputs["testRunTitle"]
    assert value == "${{ parameters.testRunTitle }}"
