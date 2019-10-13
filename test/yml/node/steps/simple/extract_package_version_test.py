from test.test_utilities import parse_node_simple_step_template_yaml_file

contents = parse_node_simple_step_template_yaml_file(
    "extract-package-version.yml"
)
steps = contents["steps"]
parameters = contents["parameters"]
step = steps[0]


def test_task_display_name_parameter_default():
    assert parameters["taskDisplayName"] == "Install dependencies"


def test_task_variable_name_parameter_default():
    assert parameters["variableName"] == "packageVersion"


def test_task_working_directory_parameter_default():
    assert parameters["workingDirectory"] == ""


def test_num_steps():
    assert len(steps) == 1


def test_step_script():
    assert step["script"] == (
        "export PACKAGE_VERSION=$(node -e "
        "\"console.log(require('./package.json').version);\")\n"
        'echo "##vso[task.setvariable variable=${{ parameters.variableName }}]'
        '$PACKAGE_VERSION"\n'
    )


def test_step_display_name():
    assert step["displayName"] == "${{ parameters.taskDisplayName }}"


def test_step_working_directory():
    assert step["workingDirectory"] == "${{ parameters.workingDirectory }}"
