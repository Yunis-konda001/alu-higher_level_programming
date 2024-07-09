#!/usr/bin/python3
"""
This module defines a class BaseGeometry with an area method
that raises an Exception.
"""


class BaseGeometry:
    """
    A class for geometry operations.
    """

    def area(self):
        """
        Raises an exception indicating that the area method is not implemented.

        Raises:
            Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")
