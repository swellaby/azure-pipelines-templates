from yaml import load
from os.path import abspath, dirname, join

yaml_root = abspath(join(dirname(dirname(__file__)), "templates", "yml"))


def get_path(filepath):
    print(yaml_root)
    return abspath(join(yaml_root, filepath))


def parse_template_yaml_file(filepath):
    contents = load(open(get_path(filepath), "r"))
    return contents
