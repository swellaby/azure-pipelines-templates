from test.test_utilities import parse_node_combo_template_yaml_file

fileName = "npm-test-lint-validation-xunit.yml"
contents = parse_node_combo_template_yaml_file(fileName)
steps = contents["steps"]
parameters = contents["parameters"]
npmInstallParameters = parameters["npmInstall"]
npmTestScriptParameters = parameters["npmTestScript"]
npmLintScriptParameters = parameters["npmLintScript"]
publishTestResultsParameters = parameters["publishTestResults"]
npmInstallStep = steps[0]
npmInstallStepParameters = npmInstallStep["parameters"]
npmTestScriptStep = steps[1]
npmTestScriptStepParameters = npmTestScriptStep["parameters"]
npmLintScriptStep = steps[2]
npmLintScriptStepParameters = npmLintScriptStep["parameters"]
publishTestResultsStep = steps[3]
publishTestResultsStepParameters = publishTestResultsStep["parameters"]


def test_npm_install_step_display_name_parameter_default():
    assert npmInstallParameters["taskDisplayName"] == "Install dependencies"


def test_npm_test_script_step_script_name_name_parameter_default():
    assert npmTestScriptParameters["npmTestScriptName"] == "test"


def test_npm_test_script_step_display_name_parameter_default():
    assert npmTestScriptParameters["taskDisplayName"] == "Run tests"


def test_npm_lint_script_step_script_name_parameter_default():
    assert npmLintScriptParameters["npmLintScriptName"] == "lint"


def test_npm_lint_script_step_display_name_parameter_default():
    assert npmLintScriptParameters["taskDisplayName"] == "Lint"


def test_publish_test_results_step_results_format_parameter_default():
    assert publishTestResultsParameters["testResultsFormat"] == "JUnit"


def test_publish_test_results_step_results_files_parameter_default():
    assert publishTestResultsParameters["testResultsFiles"] == "xunit.xml"


def test_publish_test_results_step_search_folder_parameter_default():
    value = publishTestResultsParameters["searchFolder"]
    assert value == "$(Build.SourcesDirectory)/.testresults/unit"


def test_publish_test_results_step_run_title_parameter_default():
    value = publishTestResultsParameters["testRunTitle"]
    assert value == "Unit Tests::Build $(Build.BuildId)"


def test_publish_test_results_step_task_display_name_parameter_default():
    value = publishTestResultsParameters["taskDisplayName"]
    assert value == "Publish unit test results"


def test_num_steps():
    assert len(steps) == 4


def test_npm_install_step_template_path():
    assert npmInstallStep["template"] == "../steps/simple/npm-install.yml"


def test_npm_install_step_display_name_parameter():
    value = npmInstallStepParameters["taskDisplayName"]
    assert value == "${{ parameters.npmInstall.taskDisplayName }}"


def test_npm_test_script_step_template_path():
    value = npmTestScriptStep["template"]
    assert value == "../steps/simple/npm-run-test.yml"


def test_npm_test_script_step_script_name_parameter():
    value = npmTestScriptStepParameters["testNpmScriptName"]
    assert value == "${{ parameters.npmTestScript.npmTestScriptName }}"


def test_npm_test_step_display_name_parameter():
    value = npmTestScriptStepParameters["taskDisplayName"]
    assert value == "${{ parameters.npmTestScript.taskDisplayName }}"


def test_npm_lint_script_step_template_path():
    value = npmLintScriptStep["template"]
    assert value == "../steps/simple/npm-run-lint.yml"


def test_npm_lint_script_step_script_name_parameter():
    value = npmLintScriptStepParameters["lintNpmScriptName"]
    assert value == "${{ parameters.npmLintScript.npmLintScriptName }}"


def test_npm_lint_step_display_name_parameter():
    value = npmLintScriptStepParameters["taskDisplayName"]
    assert value == "${{ parameters.npmLintScript.taskDisplayName }}"


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
