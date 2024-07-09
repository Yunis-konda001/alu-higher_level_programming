#!/usr/bin/python3
"""
Define a function is_kind_of_class that returns True if the object is an instance of,
or if the object is an instance of a class that inherited from, the specified class; otherwise False.
"""

def is_kind_of_class(obj, a_class):
    """
    Check if obj is an instance of a_class or an instance of a class that inherited from a_class.

    Parameters:
    - obj: The object to check.
    - a_class: The class to compare against.

    Returns:
    - True if obj is an instance of a_class or an instance of a subclass of a_class, False otherwise.
    """
    return isinstance(obj, a_class)
