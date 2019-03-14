from yaml import load, FullLoader
from os.path import abspath, dirname, join

yaml_root = abspath(join(dirname(dirname(__file__)), "templates", "yml"))
any_root = abspath(join(yaml_root, "any"))
node_root = abspath(join(yaml_root, "node"))
node_steps_root = abspath(join(node_root, "steps"))
node_simple_steps_root = abspath(join(node_steps_root, "simple"))
node_combo_root = abspath(join(node_root, "combo"))
python_root = abspath(join(yaml_root, "python"))
python_steps_root = abspath(join(python_root, "steps"))
python_combo_root = abspath(join(python_root, "combo"))
rust_root = abspath(join(yaml_root, "rust"))
rust_steps_root = abspath(join(rust_root, "steps"))


def get_path(root, filepath):
    return abspath(join(root, filepath))


def parse_template_yaml_file(root, filepath):
    return load(open(get_path(root, filepath), "r"), Loader=FullLoader)


def parse_any_template_yaml_file(filepath):
    return parse_template_yaml_file(any_root, filepath)


def parse_node_step_template_yaml_file(filepath):
    return parse_template_yaml_file(node_steps_root, filepath)


def parse_node_simple_step_template_yaml_file(filepath):
    return parse_template_yaml_file(node_simple_steps_root, filepath)


def parse_python_combo_template_yaml_file(filepath):
    return parse_template_yaml_file(node_combo_root, filepath)


def parse_python_step_template_yaml_file(filepath):
    return parse_template_yaml_file(python_steps_root, filepath)


def parse_python_combo_template_yaml_file(filepath):
    return parse_template_yaml_file(python_combo_root, filepath)


def parse_rust_step_template_yaml_file(filepath):
    return parse_template_yaml_file(rust_steps_root, filepath)
