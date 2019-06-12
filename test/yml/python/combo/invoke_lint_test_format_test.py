from test.test_utilities import parse_python_combo_template_yaml_file

contents = parse_python_combo_template_yaml_file("invoke-lint-test-format.yml")
steps = contents["steps"]
parameters = contents["parameters"]
setupParameters = parameters["setup"]
setVersionParameters = setupParameters["setVersion"]
pipInstallParameters = setupParameters["pipInstall"]

setupPipStep = steps[0]
setupStepParameters = setupPipStep["parameters"]
setVersionStepParameters = setupStepParameters["setVersion"]
pipInstallStepParameters = setupStepParameters["pipInstall"]

lintStep = steps[1]
lintStepParameters = lintStep["parameters"]


def test_setup_set_version_version_spec_parameter_default():
    assert setVersionParameters["versionSpec"] == "3.7"


def test_setup_set_version_architecture_parameter_default():
    assert setVersionParameters["architecture"] == "x64"


def test_setup_set_version_task_display_name_parameter_default():
    assert setVersionParameters["taskDisplayName"] == "Set python version"


def test_pip_install_requirements_file_parameter_default():
    assert pipInstallParameters["requirementsFile"] == "requirements.txt"


def test_pip_install_task_display_name_parameter_default():
    assert pipInstallParameters["taskDisplayName"] == "Install dependencies"


def test_num_steps():
    assert len(steps) == 2


def test_set_version_step_template_path():
    assert setupPipStep["template"] == "./setup-pip.yml"


def test_setup_pip_step_set_version_version_spec_parameter():
    value = setVersionStepParameters["versionSpec"]
    assert value == "${{ parameters.setup.setVersion.versionSpec }}"


def test_setup_pip_step_set_version_architecture_parameter():
    value = setVersionStepParameters["architecture"]
    assert value == "${{ parameters.setup.setVersion.architecture }}"


def test_setup_pip_step_set_version_display_name_parameter():
    value = setVersionStepParameters["taskDisplayName"]
    assert value == "${{ parameters.setup.setVersion.taskDisplayName }}"


def test_setup_pip_step_pip_install_requirements_file_parameter():
    value = pipInstallStepParameters["requirementsFile"]
    assert value == "${{ parameters.setup.pipInstall.requirementsFile }}"


def test_setup_pip_step_pip_install_display_name_parameter():
    value = pipInstallStepParameters["taskDisplayName"]
    assert value == "${{ parameters.setup.pipInstall.taskDisplayName }}"

def test_lint_step_template_path():
    assert lintStep["template"] == "../steps/run-invoke.yml"

def test_lint_step_invoke_options_parameter():
    value = lintStepParameters["invokeOptions"]
    assert value == "${{ parameters.lint.invokeOptions }}"


def test_lint_step_tasks_and_arguments_parameter():
    value = lintStepParameters["tasksAndArguments"]
    assert value == "${{ parameters.lint.tasksAndArguments }}"


def test_lint_step_display_name_parameter():
    value = lintStepParameters["taskDisplayName"]
    assert value == "${{ parameters.lint.taskDisplayName }}"
