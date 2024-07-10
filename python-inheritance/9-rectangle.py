#!/usr/bin/python3
"""
Rectangle module inheriting from BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    Rectangle class inheriting from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance.
        Args:
            width (int): width of the rectangle (positive integer).
            height (int): height of the rectangle (positive integer).
        """
        self.__width = 0
        self.__height = 0

        self.width = width
        self.height = height

    @property
    def width(self):
        """ Getter for __width private attribute """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for __width private attribute """
        self.integer_validator("width", value)
        self.__width = value

    @property
    def height(self):
        """ Getter for __height private attribute """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for __height private attribute """
        self.integer_validator("height", value)
        self.__height = value

    def area(self):
        """
        Returns the area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
