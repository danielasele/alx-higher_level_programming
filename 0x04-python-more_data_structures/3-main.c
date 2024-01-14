#!/usr/bin/python3

def common_elements(set_1, set_2):
    """
    Returns a set of common elements in two sets.

    Args:
    - set_1: The first set.
    - set_2: The second set.

    Returns:
    - A set containing common elements from both sets.
    """
    common_set = set_1.intersection(set_2)
    return common_set
