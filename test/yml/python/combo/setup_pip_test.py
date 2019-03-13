from test.test_utilities import parse_python_combo_template_yaml_file

contents = parse_python_combo_template_yaml_file("setup-pip.yml")
steps = contents["steps"]
parameters = contents["parameters"]
setVersionParameters = parameters["setVersion"]
pipInstallParameters = parameters["pipInstall"]
setVersionStep = steps[0]
setVersionStepParameters = setVersionStep["parameters"]
updateToolsStep = steps[1]
pipInstallStep = steps[2]
pipInstallStepParameters = pipInstallStep["parameters"]


def test_set_version_spec_parameter_default():
    assert setVersionParameters["versionSpec"] == "3.7"


def test_set_version_architecture_parameter_default():
    assert setVersionParameters["architecture"] == "x64"


def test_set_version_task_display_name_parameter_default():
    assert setVersionParameters["taskDisplayName"] == "Set python version"


def test_pip_install_requirements_file_parameter_default():
    assert pipInstallParameters["requirementsFile"] == "requirements.txt"


def test_pip_install_task_display_name_parameter_default():
    assert pipInstallParameters["taskDisplayName"] == "Install dependencies"


def test_num_steps():
    assert len(steps) == 3


def test_set_version_step_template_path():
    assert setVersionStep["template"] == "../steps/set-version.yml"


def test_set_version_step_version_spec_parameter():
    value = setVersionStepParameters["versionSpec"]
    assert value == "${{ parameters.setVersion.versionSpec }}"


def test_set_version_step_architecture_parameter():
    value = setVersionStepParameters["architecture"]
    assert value == "${{ parameters.setVersion.architecture }}"


def test_set_version_step_display_name_parameter():
    value = setVersionStepParameters["taskDisplayName"]
    assert value == "${{ parameters.setVersion.taskDisplayName }}"


def test_update_tools_step_template_path():
    value = updateToolsStep["template"]
    assert value == "../steps/update-tools.yml"


def test_pip_install_step_template_path():
    value = pipInstallStep["template"]
    assert value == "../steps/pip-install.yml"


def test_pip_install_step_requirements_file_parameter():
    value = pipInstallStepParameters["requirementsFile"]
    assert value == "${{ parameters.pipInstall.requirementsFile }}"


def test_pip_install_step_display_name_parameter():
    value = pipInstallStepParameters["taskDisplayName"]
    assert value == "${{ parameters.pipInstall.taskDisplayName }}"
