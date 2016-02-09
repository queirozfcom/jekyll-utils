from pathlib import Path

import os


def resolve_path(path, strip_trailing_slash=True):
    if strip_trailing_slash:
        path = path.rstrip("/")

    if Path(path).is_absolute():
        absolute_path = path
    else:
        absolute_origin = os.getcwd()
        absolute_path = absolute_origin + "/" + path

    return absolute_path


def list_files(absolute_directory, keywords):
    """
    Returns all files under absolute_directory that contain all given keywords.

    :param absolute_directory:
    :param keywords: a tuple containing the keywords that should match
    :return: a list of the filenames matching given keywords,
    """

    matches = []

    for root, dirnames, filenames in os.walk(absolute_directory):
        for filename in _filter_match_all(filenames, keywords):
            matches.append(os.path.join(root, filename))

    # remove the paths, return only file names
    prefix = absolute_directory.rstrip('/') + '/'
    len_prefix = len(prefix)

    # http://stackoverflow.com/a/600195/436721
    return list(map(lambda full_path: full_path[len_prefix:], matches))


def _filter_match_all(elements, keywords):
    """
    Returns the elements for which all keywords are contained.

    :param elements: a list of strings to filter
    :param keywords: a tuple containing keywords that should all be included
    :return: matching matching elements
    """
    matching = []

    for elem in elements:
        if all(keyword in elem for keyword in keywords):
            matching.append(elem)

    return matching
