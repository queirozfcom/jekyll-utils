import errno
import sys

import os
import toml
from appdirs import user_config_dir
from jekyllutils.helpers.colours import with_error_prefix, wrap_yellow, with_success_prefix


def get_posts_path():
    return _get_config("posts-path")


def get_editor_name():
    return _get_config("editor")


def clear_configs():
    _create_config_file_if_needed()
    with(open(_get_config_file(), "w")) as f:
        f.write("")


def dump_configs():
    """
    Outputs the contents of this project's config file
    """
    _create_config_file_if_needed()
    print("\n==Dump Config file==\n")
    print("Location: {0}\n".format(_get_config_file()))
    print("Contents:\n")
    with open(_get_config_file()) as f:
        print(f.read())


def set_editor_name(name):
    _set_config("editor", name)


def set_posts_path_dir(path):
    _set_config("posts-path", path)


# private

def _set_config(name, value):
    _create_config_file_if_needed()

    with open(_get_path_to_config_file(), "a+") as f:

        # move the pointer to the start because we want to read the file first
        f.seek(0)
        config = toml.loads(f.read())
        config[name] = value
        new_conf = toml.dumps(config)

        # then delete everything and write the new config
        f.truncate(0)
        f.seek(0)
        f.write(new_conf)



def _get_config(name):
    try:
        with open(_get_path_to_config_file()) as f:
            config = toml.loads(f.read())
            return config[name]
    except KeyError as e:

        sample_command = f"jk-config-set-{name} foo-bar"

        print(with_error_prefix(
            f"""Please set a value for key "{name}" in the config.\nFor example: {wrap_yellow(sample_command)}"""))
        sys.exit(1)


def _create_config_file_if_needed():
    filename = _get_path_to_config_file()

    if os.path.isfile(filename):
        return
    else:
        if not os.path.exists(os.path.dirname(filename)):
            try:
                os.makedirs(os.path.dirname(filename))
            except OSError as exc:  # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise

        with open(filename, "w") as f:
            print(with_success_prefix(f"Created new config file at: {filename}"))
            f.write("")


def _get_path_to_config_file():
    return user_config_dir("jekyll-utils", "queirozfcom") + "/config.toml"


def _raise_error_if_no_config():
    if not os.path.isfile(_get_path_to_config_file()):
        raise FileNotFoundError("Config file not found")
