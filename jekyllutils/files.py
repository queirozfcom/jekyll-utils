import os
import re
from pathlib import Path

from jekyllutils.helpers.colours import wrap_yellow, wrap_blue, wrap_green
from jekyllutils.helpers.text import match_all, filter_match_all


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
        for filename in filter_match_all(filenames, keywords):
            matches.append(os.path.join(root, filename))

    # remove the paths, return only file names
    prefix = absolute_directory.rstrip('/') + '/'
    len_prefix = len(prefix)

    # http://stackoverflow.com/a/600195/436721
    return list(map(lambda full_path: full_path[len_prefix:], matches))


def list_filenames_by_tag(absolute_directory, tags):
    """
    Returns all filenames under absolute_directory that contain all given tags.

    :param absolute_directory:
    :param keywords: a tuple containing the tags the post should have
    :return: a list of the filenames matching given tags,
    """
    matches = []

    for root, _, filenames in os.walk(absolute_directory):
        for filename in filenames:
            absolute_path_to_file = os.path.join(root, filename)

            with open(absolute_path_to_file, "r") as f:

                contents = f.read().lower().strip()

                if _has_tags(contents, tags):

                    if _is_not_published(contents):
                        prefix = wrap_yellow("[UNP] ")
                        matches.append(f"{prefix} {filename}")
                        continue

                    if _is_wip(contents):
                        prefix = wrap_blue("[WIP] ")
                        matches.append(f"{prefix} {filename}")
                        continue

                    # if the file is published, check for TODOs
                    if _is_todo(contents):
                        prefix = wrap_green("[TODO]")
                        matches.append(f"{prefix} {filename}")
                        continue
                        
                    matches.append(filename)

    return matches


def list_unpublished_filenames(absolute_directory, include_wip):
    """
    Returns all filenames under absolute_directory that are unpublished.
    (i.e. files where published: false in front-matter)

    :param absolute_directory:
    :param include_wip: if true, also return files that contain "wip alert" and "TODO"
    :return: a list of the filenames
    """
    matches = []

    for root, _, filenames in os.walk(absolute_directory):
        for filename in filenames:
            absolute_path_to_file = os.path.join(root, filename)

            with open(absolute_path_to_file, "r") as f:

                contents = f.read().lower().strip()

                if _is_not_published(contents):
                    prefix = wrap_yellow("[UNP] ")
                    matches.append(f"{prefix} {filename}")
                    continue

                if include_wip and _is_wip(contents):
                    prefix = wrap_blue("[WIP] ")
                    matches.append(f"{prefix} {filename}")
                    continue

                # if the file is published, check for TODOs
                if include_wip and _is_todo(contents):
                    prefix = wrap_green("[TODO]")
                    matches.append(f"{prefix} {filename}")
                    continue

    return list(set(matches))


def _has_tags(contents: str, tags: tuple):
    for line in contents.lower().splitlines():
        if line.strip().startswith("tags:"):
            if match_all(line, tags):
                return True

    return False


def _is_not_published(contents):
    """
    Checks if the contents of a file are not published.
    :param contents: the contents of the file
    :return: True if the file is not published, False otherwise
    """
    return "published: false" in contents or "published: false\n" in contents or "published: false " in contents


def _is_wip(contents):
    for line in contents.splitlines():
        line_clean = line.strip().lower()

        if "wip alert" in line_clean:
            return True

    return False


def _is_todo(contents):
    for line in contents.splitlines():
        line_clean = line.strip().lower()

        if (re.search("todo: ", line_clean) or
            re.search("todo\n", line_clean) or
            re.search("^todo ", line_clean) or
            re.search(" todo ", line_clean)):
            return True

    return False
