from test.test_utilities import parse_python_combo_template_yaml_file

contents = parse_python_combo_template_yaml_file("run-pytest-ci.yml")
steps = contents["steps"]
parameters = contents["parameters"]
testParameters = parameters["test"]
publishTestResultsParameters = parameters["publishTestResults"]
testStep = steps[0]
testStepParameters = testStep["parameters"]
publishTestResultsStep = steps[1]
publishTestResultsStepParameters = publishTestResultsStep["parameters"]


def test_test_step_additional_args_parameter_default():
    value = testParameters["additionalArgs"]
    assert value == "--junitxml=.testresults/unit/junit.xml"


def test_test_step_task_display_name_parameter_default():
    assert testParameters["taskDisplayName"] == "Run unit tests"


def test_publish_step_results_format_parameter_default():
    assert publishTestResultsParameters["testResultsFormat"] == "JUnit"


def test_publish_step_results_files_parameter_default():
    assert publishTestResultsParameters["testResultsFiles"] == "junit.xml"


def test_publish_step_search_folder_parameter_default():
    value = publishTestResultsParameters["searchFolder"]
    assert value == "$(Build.SourcesDirectory)/.testresults/unit"


def test_publish_step_run_title_parameter_default():
    value = publishTestResultsParameters["testRunTitle"]
    assert value == "Unit Tests::Build $(Build.BuildId)"


def test_publish_step_task_display_name_parameter_default():
    value = publishTestResultsParameters["taskDisplayName"]
    assert value == "Publish unit test results"


def test_num_steps():
    assert len(steps) == 2


def test_pytest_step_template_path():
    assert testStep["template"] == "../steps/pytest.yml"


def test_pytest_step_additional_args_parameter():
    value = testStepParameters["additionalArgs"]
    assert value == "${{ parameters.test.additionalArgs }}"


def test_pytest_step_display_name_parameter():
    value = testStepParameters["taskDisplayName"]
    assert value == "${{ parameters.test.taskDisplayName }}"


def test_publish_step_template_path():
    value = publishTestResultsStep["template"]
    assert value == "../../any/publish-test-results.yml"


def test_publish_step_test_results_format_parameter():
    value = publishTestResultsStepParameters["testResultsFormat"]
    assert value == "${{ parameters.publishTestResults.testResultsFormat }}"


def test_publish_step_test_results_files_parameter():
    value = publishTestResultsStepParameters["testResultsFiles"]
    assert value == "${{ parameters.publishTestResults.testResultsFiles }}"


def test_publish_step_search_folder_parameter():
    value = publishTestResultsStepParameters["searchFolder"]
    assert value == "${{ parameters.publishTestResults.searchFolder }}"


def test_publish_step_test_run_title_parameter():
    value = publishTestResultsStepParameters["testRunTitle"]
    assert value == "${{ parameters.publishTestResults.testRunTitle }}"


def test_publish_step_display_name_parameter():
    value = publishTestResultsStepParameters["taskDisplayName"]
    assert value == "${{ parameters.publishTestResults.taskDisplayName }}"
