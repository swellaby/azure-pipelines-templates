from test.test_utilities import parse_any_template_yaml_file

template = "sonar/run-sonar-cloud-cli-analysis.yml"
contents = parse_any_template_yaml_file(template)
steps = contents["steps"]
parameters = contents["parameters"]
sonarPrepStep = steps[0]
sonarPrepStepInputs = sonarPrepStep["inputs"]
sonarRunStep = steps[1]
sonarPublishStep = steps[2]


def test_num_steps():
    assert len(steps) == 3


def test_sonar_cloud_endpoint_parameter_default():
    assert parameters["sonarCloudEndpoint"] == "SonarCloud Swellaby"


def test_organization_parameter_default():
    assert parameters["organization"] == "swellaby"


def test_project_version_parameter_default():
    assert parameters["projectVersion"] == "$(Build.BuildId)"


def test_prep_step_type():
    exp = (
        "SonarSource.sonarcloud."
        "14d9cde6-c1da-4d55-aa01-2965cd301255."
        "SonarCloudPrepare@1"
    )
    assert sonarPrepStep["task"] == exp


def test_prep_step_display_name():
    assert sonarPrepStep["displayName"] == "Prepare analysis on SonarCloud"


def test_prep_step_sonar_cloud_input():
    exp = "${{ parameters.sonarCloudEndpoint }}"
    assert sonarPrepStepInputs["SonarCloud"] == exp


def test_prep_step_organization_input():
    value = sonarPrepStepInputs["organization"]
    assert value == "${{ parameters.organization }}"


def test_prep_step_scanner_mode_input():
    assert sonarPrepStepInputs["scannerMode"] == "CLI"


def test_prep_step_extra_properties_input():
    value = sonarPrepStepInputs["extraProperties"]
    assert value == "sonar.projectVersion=${{ parameters.projectVersion }}\n"


def test_run_step_type():
    exp = (
        "SonarSource.sonarcloud."
        "ce096e50-6155-4de8-8800-4221aaeed4a1."
        "SonarCloudAnalyze@1"
    )
    assert sonarRunStep["task"] == exp


def test_run_step_display_name():
    assert sonarRunStep["displayName"] == "Run Sonar analysis"


def test_publish_step_type():
    exp = (
        "SonarSource.sonarcloud."
        "38b27399-a642-40af-bb7d-9971f69712e8."
        "SonarCloudPublish@1"
    )
    assert sonarPublishStep["task"] == exp


def test_publish_step_display_name():
    assert sonarPublishStep["displayName"] == "Publish quality gate result"
