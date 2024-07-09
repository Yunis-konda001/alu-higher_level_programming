#!/usr/bin/python3
"""
This module defines a function inheritance.
of a class that inherited (directly or indirectly) from the specified class.
"""


def inherits_from(obj, a_class):
    """
    Function to check if obj is an instance of a class that inherited
    (directly or indirectly) from a_class, excluding a_class itself.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
    True if obj is an instance of a class that inherited from a_class
    False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
