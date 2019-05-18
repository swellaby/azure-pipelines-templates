from test.test_utilities import parse_rust_step_template_yaml_file

contents = parse_rust_step_template_yaml_file("cargo-build.yml")
parameters = contents["parameters"]
steps = contents["steps"]
step = steps[0]


def test_display_name_parameter_default():
    assert parameters["taskDisplayName"] == "build"


def test_num_steps():
    assert len(steps) == 1


def test_script_contents():
    assert step["script"] == "cargo build ${{ parameters.additionalArgs }}"


def test_script_display_name():
    assert step["displayName"] == "${{ parameters.taskDisplayName }}"
