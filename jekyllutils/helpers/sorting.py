import re


def sort_filenames_ignoring_leading_text(list_of_filenames, reverse=None):
    """
    need a custom function because we don't want strings starting with [...] before everything else

    :param list_of_prefixed_filenames: list of strings of the form ".... yyyy-mm-dd-post-title-slug.markdown"
    :param reverse:
    :return:
    """

    if reverse is None:
        reverse = False

    leading_pattern_to_remove = r"""(^[^]]+\]\s?[^\s]+\s|^\s+)"""

    return sorted(list_of_filenames, key=lambda a: re.sub(leading_pattern_to_remove, "", a), reverse=reverse)
