import os
from pathlib import Path


def resolve_path(path, strip_trailing_slash=True):
    if strip_trailing_slash:
        path = path.rstrip("/")

    if Path(path).is_absolute():
        absolute_path = path
    else:
        absolute_origin = os.getcwd()
        absolute_path = absolute_origin + "/" + path

    return absolute_path
