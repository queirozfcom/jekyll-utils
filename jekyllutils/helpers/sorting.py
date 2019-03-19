import re


def sort_ignoring_brackets(list_of_filenames, reverse=None):
    """
    need a custom function because we don't want strings starting with [...] before everything else

    :param list_of_filenames:
    :param reverse:
    :return:
    """

    if reverse is None:
        reverse = False

    return sorted(list_of_filenames, key=lambda a: re.sub("(?i)^\[\w+\]\s*", "", a), reverse=reverse)
