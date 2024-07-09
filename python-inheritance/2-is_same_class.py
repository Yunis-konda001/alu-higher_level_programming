#!/usr/bin/python3
"""
Define a function is_same_class that returns True if the object is exactly an instance of the specified class, otherwise False.
"""

def is_same_class(obj, a_class):
    """
    Check if obj is exactly an instance of a_class.

    Parameters:
    - obj: The object to check.
    - a_class: The class to compare against.

    Returns:
    - True if obj is exactly an instance of a_class, False otherwise.
    """
    return type(obj) is a_class
