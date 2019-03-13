from yaml import load
from os.path import abspath, dirname, join

yaml_root = abspath(join(dirname(dirname(__file__)), "templates", "yml"))
any_root = abspath(join(yaml_root, "any"))
python_root = abspath(join(yaml_root, "python"))
python_steps_root = abspath(join(python_root, "steps"))
python_combo_root = abspath(join(python_root, "combo"))
rust_root = abspath(join(yaml_root, "rust"))
rust_steps_root = abspath(join(rust_root, "steps"))


def get_path(root, filepath):
    return abspath(join(root, filepath))


def parse_template_yaml_file(root, filepath):
    return load(open(get_path(root, filepath), "r"))


def parse_any_template_yaml_file(filepath):
    return parse_template_yaml_file(any_root, filepath)


def parse_python_step_template_yaml_file(filepath):
    return parse_template_yaml_file(python_steps_root, filepath)


def parse_python_combo_template_yaml_file(filepath):
    return parse_template_yaml_file(python_combo_root, filepath)


def parse_rust_step_template_yaml_file(filepath):
    return parse_template_yaml_file(rust_steps_root, filepath)
