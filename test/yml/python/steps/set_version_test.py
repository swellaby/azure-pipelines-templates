from test.test_utilities import parse_python_step_template_yaml_file

contents = parse_python_step_template_yaml_file("set-version.yml")
steps = contents["steps"]
parameters = contents["parameters"]
usePythonVersionStep = steps[0]
usePythonVersionInputs = usePythonVersionStep["inputs"]


def test_version_spec_parameter_default():
    assert parameters["versionSpec"] == "3.7"


def test_architecture_parameter_default():
    assert parameters["architecture"] == "x64"


def test_task__display_name_parameter_default():
    assert parameters["taskDisplayName"] == "Set python version"


def test_num_steps():
    assert len(steps) == 1


def test_step_type():
    assert usePythonVersionStep["task"] == "UsePythonVersion@0"


def test_step_display_name():
    assert usePythonVersionStep["displayName"] == (
        "${{ parameters.taskDisplayName }}"
    )


def test_step_version_spec_input():
    assert usePythonVersionInputs["versionSpec"] == (
        "${{ parameters.versionSpec }}"
    )


def test_step_architecture_input():
    assert usePythonVersionInputs["architecture"] == (
        "${{ parameters.architecture }}"
    )
