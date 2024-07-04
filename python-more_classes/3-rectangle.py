#!/usr/bin/python3
"""
This module defines a Rectangle class.
"""


class Rectangle:
    """
    This class represents a rectangle.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance.

        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method for width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width attribute."""
        self.__validate_dimension(value, "width")
        self.__width = value

    @property
    def height(self):
        """Getter method for height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height attribute."""
        self.__validate_dimension(value, "height")
        self.__height = value

    def __validate_dimension(self, value, dimension):
        """
        Validates a dimension value (width or height).

        Args:
            value (int): The value of the dimension.
            dimension (str): The dimension name ("width" or "height").

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is
