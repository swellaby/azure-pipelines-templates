from test.test_utilities import parse_python_step_template_yaml_file

contents = parse_python_step_template_yaml_file("run-invoke.yml")
steps = contents["steps"]
parameters = contents["parameters"]
first = steps[0]


def test_invoke_options_parameter_default():
    assert parameters["invokeOptions"] == ""


def test_tasks_and_arguments_parameter_default():
    assert parameters["tasksAndArguments"] == ""


def test_task_display_name_parameter_default():
    assert parameters["taskDisplayName"] == "Run Invoke"


def test_step_display_name():
    assert first["displayName"] == "${{ parameters.taskDisplayName }}"


def test_num_steps():
    assert len(steps) == 1


def test_script_contents():
    assert first["script"] == (
        "invoke "
        "${{ parameters.invokeOptions }} "
        "${{ parameters.tasksAndArguments }}"
    )
