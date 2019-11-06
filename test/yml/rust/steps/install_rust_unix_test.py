from test.test_utilities import parse_rust_step_template_yaml_file

contents = parse_rust_step_template_yaml_file("install-rust-unix.yml")
parameters = contents["parameters"]
steps = contents["steps"]
step = steps[0]


def test_display_name_parameter_default():
    assert parameters["taskDisplayName"] == "Install Rust"


def test_num_steps():
    assert len(steps) == 1


def test_script_contents():
    assert step["script"] == (
        "set -eo pipefail\n"
        "curl https://sh.rustup.rs -sSf | sh -s -- -y\n"
        'echo "##vso[task.setvariable variable=PATH;]'
        '$PATH:$HOME/.cargo/bin"\n'
        'echo "##vso[task.setvariable variable=cargoBinPath;]'
        '$HOME/.cargo/bin"\n'
    )


def test_script_display_name():
    assert step["displayName"] == "${{ parameters.taskDisplayName }}"
