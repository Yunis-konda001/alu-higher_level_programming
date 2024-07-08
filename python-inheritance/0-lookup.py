#!/usr/bin/env python3
def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.
    
    Args:
    - obj: Any Python object
    
    Returns:
    - list: List of strings containing attribute and method names
    """
    return dir(obj)
