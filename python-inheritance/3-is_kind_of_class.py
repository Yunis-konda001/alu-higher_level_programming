#!/usr/bin/python3
"""
Define a function is_kind_of_class.
or if the object is an instance of a class.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if obj is an instance of a_class or an instance.

    Parameters:
    - obj: The object to check.
    - a_class: The class to compare against.

    Returns:
    - True if obj is an instance of a_class.
    """
    return isinstance(obj, a_class)
