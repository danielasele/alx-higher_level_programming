#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """
    Prints a dictionary by ordered keys.

    Args:
    - a_dictionary: The input dictionary.

    Note:
    - Keys are sorted by alphabetic order.
    - Only sort keys of the first level (don’t sort keys of a dictionary inside the main dictionary).
    - Dictionary values can have any type.
    """
    sorted_keys = sorted(a_dictionary.keys())

    for key in sorted_keys:
        print("{}: {}".format(key, a_dictionary[key]))
