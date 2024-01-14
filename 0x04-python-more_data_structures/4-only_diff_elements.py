#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """
    Returns a set of all elements present in only one set.

    Args:
    - set_1: The first set.
    - set_2: The second set.

    Returns:
    - A set containing elements present in only one of the sets.
    """
    diff_set = set_1.symmetric_difference(set_2)
    return diff_set
