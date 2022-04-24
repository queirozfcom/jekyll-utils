def match_all(s, keywords):
    """
    True if all strings in keywords are contained in s, False otherwise.
    Case-insensitive.

    :param s: string
    :param keywords: a tuple containing keywords that should all be included
    :return: True if all strings in keywords are contained in s, False otherwise
    """

    for kw in keywords:
        if kw.lower().strip() not in s.lower().strip():
            return False

    return True


def filter_match_all(elements, keywords):
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
