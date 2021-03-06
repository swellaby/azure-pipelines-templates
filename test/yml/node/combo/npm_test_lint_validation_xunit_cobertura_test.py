from test.test_utilities import parse_node_combo_template_yaml_file

fileName = "npm-test-lint-validation-xunit-cobertura.yml"
contents = parse_node_combo_template_yaml_file(fileName)
steps = contents["steps"]
parameters = contents["parameters"]
npmInstallParameters = parameters["npmInstall"]
npmTestScriptParameters = parameters["npmTestScript"]
npmLintScriptParameters = parameters["npmLintScript"]
publishTestResultsParameters = parameters["publishTestResults"]
publishCoverageResultsParameters = parameters["publishCoverage"]
validationStep = steps[0]
validationStepParameters = validationStep["parameters"]
npmInstallStepParameters = validationStepParameters["npmInstall"]
npmTestScriptStepParameters = validationStepParameters["npmTestScript"]
npmLintScriptStepParameters = validationStepParameters["npmLintScript"]
publishTestResultsStepParameters = validationStepParameters[
    "publishTestResults"
]
publishCodeCoverageStep = steps[1]
publishCodeCoverageStepParameters = publishCodeCoverageStep["parameters"]


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


def test_publish_code_coverage_step_code_coverage_tool_parameter_default():
    assert publishCoverageResultsParameters["codeCoverageTool"] == "Cobertura"


def test_publish_code_coverage_step_summary_file_location_parameter_default():
    value = publishCoverageResultsParameters["summaryFileLocation"]
    exp = "$(Build.SourcesDirectory)/.coverage/unit/cobertura-coverage.xml"
    assert value == exp


def test_publish_code_coverage_step_report_directory_parameter_default():
    value = publishCoverageResultsParameters["reportDirectory"]
    assert value == "$(Build.SourcesDirectory)/.coverage/unit"


def test_publish_code_coverage_additional_files_parameter_default():
    value = publishCoverageResultsParameters["additionalCodeCoverageFiles"]
    assert value == ""


def test_publish_code_coverage_step_fail_if_coverage_empty_parameter_default():
    assert publishCoverageResultsParameters["failIfCoverageEmpty"] is False


def test_publish_code_coverage_step_task_display_name_parameter_default():
    value = publishCoverageResultsParameters["taskDisplayName"]
    assert value == "Publish coverage results"


def test_num_steps():
    assert len(steps) == 2


def test_npm_install_step_display_name_parameter():
    value = npmInstallStepParameters["taskDisplayName"]
    assert value == "${{ parameters.npmInstall.taskDisplayName }}"


def test_npm_test_script_step_script_name_parameter():
    value = npmTestScriptStepParameters["npmTestScriptName"]
    assert value == "${{ parameters.npmTestScript.npmTestScriptName }}"


def test_npm_test_step_display_name_parameter():
    value = npmTestScriptStepParameters["taskDisplayName"]
    assert value == "${{ parameters.npmTestScript.taskDisplayName }}"


def test_npm_lint_script_step_script_name_parameter():
    value = npmLintScriptStepParameters["npmLintScriptName"]
    assert value == "${{ parameters.npmLintScript.npmLintScriptName }}"


def test_npm_lint_step_display_name_parameter():
    value = npmLintScriptStepParameters["taskDisplayName"]
    assert value == "${{ parameters.npmLintScript.taskDisplayName }}"


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


def test_publish_code_coverage_step_template_path():
    value = publishCodeCoverageStep["template"]
    assert value == "../../any/publish-code-coverage.yml"


def test_publish_code_coverage_step_code_coverage_tool_parameter():
    value = publishCodeCoverageStepParameters["codeCoverageTool"]
    assert value == "${{ parameters.publishCoverage.codeCoverageTool }}"


def test_publish_code_coverage_step_summary_file_location_parameter():
    value = publishCodeCoverageStepParameters["summaryFileLocation"]
    exp = "${{ parameters.publishCoverage.summaryFileLocation }}"
    assert value == exp


def test_publish_code_coverage_step_report_directory_parameter():
    value = publishCodeCoverageStepParameters["reportDirectory"]
    exp = "${{ parameters.publishCoverage.reportDirectory }}"
    assert value == exp


def test_publish_code_coverage_step_additional_code_coverage_files_parameter():
    value = publishCodeCoverageStepParameters["additionalCodeCoverageFiles"]
    exp = "${{ parameters.publishCoverage.additionalCodeCoverageFiles }}"
    assert value == exp


def test_publish_code_coverage_step_fail_if_coverage_empty_parameter():
    value = publishCodeCoverageStepParameters["failIfCoverageEmpty"]
    exp = "${{ parameters.publishCoverage.failIfCoverageEmpty }}"
    assert value == exp


def test_publish_code_coverage_step_display_name_parameter():
    value = publishCodeCoverageStepParameters["taskDisplayName"]
    assert value == "${{ parameters.publishCoverage.taskDisplayName }}"
