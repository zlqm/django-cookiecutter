import os

import yaml
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

from p_config import Config


SERVER_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SERVER_DIR)
DEFAULT_CONFIG_DIR = os.path.join(BASE_DIR, 'config')


def yaml_to_json(filename):
    """convert yaml to json
    """
    filename = os.path.join(DEFAULT_CONFIG_DIR, filename)
    with open(filename) as file_obj:
        res = yaml.load(file_obj, Loader=Loader)
    return res or {}


# load configure file
default_config_file = os.path.join(DEFAULT_CONFIG_DIR, 'project.yaml')
pc = Config(default_config_file)
pc.load_env()
pc.set_cast_func('base.logging', yaml_to_json)
