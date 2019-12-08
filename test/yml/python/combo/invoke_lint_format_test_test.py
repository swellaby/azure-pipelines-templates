from test.test_utilities import parse_python_combo_template_yaml_file

contents = parse_python_combo_template_yaml_file("invoke-lint-format-test.yml")
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

formatStep = steps[2]
formatStepParameters = formatStep["parameters"]

testStep = steps[3]
testStepParameters = testStep["parameters"]

publishTestResultsStep = steps[4]
publishTestResultsStepParameters = publishTestResultsStep["parameters"]

runInvokeStepTemplatePath = "../steps/run-invoke.yml"


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
    assert len(steps) == 5


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
    assert lintStep["template"] == runInvokeStepTemplatePath


def test_lint_step_invoke_options_parameter():
    value = lintStepParameters["invokeOptions"]
    assert value == "${{ parameters.lint.invokeOptions }}"


def test_lint_step_tasks_and_arguments_parameter():
    value = lintStepParameters["tasksAndArguments"]
    assert value == "${{ parameters.lint.tasksAndArguments }}"


def test_lint_step_display_name_parameter():
    value = lintStepParameters["taskDisplayName"]
    assert value == "${{ parameters.lint.taskDisplayName }}"


def test_format_step_template_path():
    assert lintStep["template"] == runInvokeStepTemplatePath


def test_format_step_invoke_options_parameter():
    value = formatStepParameters["invokeOptions"]
    assert value == "${{ parameters.format.invokeOptions }}"


def test_format_step_tasks_and_arguments_parameter():
    value = formatStepParameters["tasksAndArguments"]
    assert value == "${{ parameters.format.tasksAndArguments }}"


def test_format_step_display_name_parameter():
    value = formatStepParameters["taskDisplayName"]
    assert value == "${{ parameters.format.taskDisplayName }}"


def test_test_step_template_path():
    assert testStep["template"] == runInvokeStepTemplatePath


def test_test_step_invoke_options_parameter():
    value = testStepParameters["invokeOptions"]
    assert value == "${{ parameters.test.invokeOptions }}"


def test_test_step_tasks_and_arguments_parameter():
    value = testStepParameters["tasksAndArguments"]
    assert value == "${{ parameters.test.tasksAndArguments }}"


def test_test_step_display_name_parameter():
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
