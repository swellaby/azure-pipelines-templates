from test.test_utilities import parse_template_yaml_file

contents = parse_template_yaml_file("rust/steps/install-rust-unix.yml")
steps = contents["steps"]
first = steps[0]


def test_display_name():
    assert first["displayName"] == "Install Rust"


def test_num_steps():
    assert len(steps) == 1


def test_script_contents():
    assert first["script"] == (
        "curl https://sh.rustup.rs -sSf | sh -s -- -y\n"
        "echo \"##vso[task.setvariable variable=PATH;]"
        "$PATH:$HOME/.cargo/bin\"\n"
        "echo \"##vso[task.setvariable variable=cargoBinPath;]"
        "$HOME/.cargo/bin\"\n"
    )
