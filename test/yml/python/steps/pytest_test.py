from test.test_utilities import parse_python_step_template_yaml_file

contents = parse_python_step_template_yaml_file("pytest.yml")
steps = contents["steps"]
parameters = contents["parameters"]
first = steps[0]


def test_additional_args_parameter_default():
    assert parameters["additionalArgs"] == ""


def test_task_display_name_parameter_default():
    assert parameters["taskDisplayName"] == "Run tests"


def test_step_display_name():
    assert first["displayName"] == "${{ parameters.taskDisplayName }}"


def test_num_steps():
    assert len(steps) == 1


def test_script_contents():
    assert first["script"] == "pytest ${{ parameters.additionalArgs }}"
