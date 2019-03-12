from test.test_utilities import parse_python_step_template_yaml_file

contents = parse_python_step_template_yaml_file("update-tools.yml")
steps = contents["steps"]
first = steps[0]


def test_step_display_name():
    assert first["displayName"] == "Install tools"


def test_num_steps():
    assert len(steps) == 1


def test_script_contents():
    assert first["script"] == (
        "python -m pip install --upgrade pip setuptools wheel"
    )
