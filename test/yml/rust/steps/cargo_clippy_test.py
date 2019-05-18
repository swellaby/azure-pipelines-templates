from test.test_utilities import parse_rust_step_template_yaml_file

contents = parse_rust_step_template_yaml_file("cargo-clippy.yml")
parameters = contents["parameters"]
steps = contents["steps"]
step = steps[0]


def test_display_name_parameter_default():
    assert parameters["taskDisplayName"] == "clippy"


def test_num_steps():
    assert len(steps) == 1


def test_script_contents():
    assert step["script"] == (
        "set -eo pipefail\n"
        "rustup component add clippy\n"
        "cargo clippy ${{ parameters.additionalArgs }}\n"
    )


def test_script_display_name():
    assert step["displayName"] == "${{ parameters.taskDisplayName }}"
