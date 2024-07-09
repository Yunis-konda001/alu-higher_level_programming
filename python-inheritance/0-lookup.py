#!/usr/bin/python3
"""
Define a function lookup that returns a list of available attributes.
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.
    """
    return dir(obj)
