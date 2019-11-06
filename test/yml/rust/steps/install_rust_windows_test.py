from test.test_utilities import parse_rust_step_template_yaml_file

contents = parse_rust_step_template_yaml_file("install-rust-windows.yml")
parameters = contents["parameters"]
steps = contents["steps"]
step = steps[0]


def test_display_name_parameter_default():
    assert parameters["taskDisplayName"] == "Install Rust"


def test_num_steps():
    assert len(steps) == 1


def test_script_contents():
    assert step["powershell"] == (
        "Invoke-WebRequest -Uri 'https://win.rustup.rs' "
        "-Method 'GET' -OutFile .\\rustup-init.exe\n"
        ".\\rustup-init.exe -y\n"
        'echo "##vso[task.setvariable variable=PATH;]'
        '$env:PATH;$env:USERPROFILE\\.cargo\\bin"\n'
        'echo "##vso[task.setvariable variable=cargoBinPath;]'
        '$env:USERPROFILE\\.cargo\\bin"\n'
    )


def test_script_display_name():
    assert step["displayName"] == "${{ parameters.taskDisplayName }}"
