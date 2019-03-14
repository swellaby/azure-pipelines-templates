from test.test_utilities import parse_node_simple_step_template_yaml_file

contents = parse_node_simple_step_template_yaml_file("npm-run-build.yml")
steps = contents["steps"]
parameters = contents["parameters"]
step = steps[0]
stepInputs = step["inputs"]


def test_task_build_npm_script_name_parameter_default():
    assert parameters["buildNpmScriptName"] == "build"


def test_task_display_name_parameter_default():
    assert parameters["taskDisplayName"] == "Run build script"


def test_step_display_name():
    assert step["displayName"] == "${{ parameters.taskDisplayName }}"


def test_num_steps():
    assert len(steps) == 1


def test_step_command_input():
    assert stepInputs["command"] == "custom"


def test_step_custom_command_input():
    value = stepInputs["customCommand"]
    assert value == "run ${{ parameters.buildNpmScriptName }}"
