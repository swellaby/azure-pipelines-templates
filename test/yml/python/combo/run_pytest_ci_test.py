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
    assert (
        testParameters["additionalArgs"]
        == "--junitxml=.testresults/unit/junit.xml"
    )


def test_test_step_task_display_name_parameter_default():
    assert testParameters["taskDisplayName"] == "Run unit tests"


# def test_architecture_parameter_default():
#     assert parameters["architecture"] == "x64"


# def test_task__display_name_parameter_default():
#     assert parameters["taskDisplayName"] == "Set python version"


# def test_num_steps():
#     assert len(steps) == 1


# def test_step_type():
#     assert usePythonVersionStep["task"] == "UsePythonVersion@0"


# def test_step_display_name():
#     assert usePythonVersionStep["displayName"] == (
#         "${{ parameters.taskDisplayName }}"
#     )


# def test_step_version_spec_input():
#     assert usePythonVersionInputs["versionSpec"] == (
#         "${{ parameters.versionSpec }}"
#     )


# def test_step_architecture_input():
#     assert usePythonVersionInputs["architecture"] == (
#         "${{ parameters.architecture }}"
#     )
