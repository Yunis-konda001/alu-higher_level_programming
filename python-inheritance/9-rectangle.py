#!/usr/bin/python3
"""
Rectangle module inheriting from BaseGeometry.
"""

class BaseGeometry:
    """
    BaseGeometry class with integer_validator method.
    """

    def __init__(self):
        pass

    def integer_validator(self, name, value):
        """
        Validates that value is an integer greater than 0.
        Args:
            name (str): Name of the value being validated.
            value (int): Value to be validated.
        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    """
    Rectangle class inheriting from BaseGeometry.
    """

    def __init__(self, width=None, height=None):
        """
        Initializes a Rectangle instance.
        Args:
            width (int, optional): Width of the rectangle (positive integer).
            height (int, optional): Height of the rectangle (positive integer).
        """
        super().__init__()
        if width is not None and height is not None:
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

# Testing the output of dir(Rectangle)
print(dir(Rectangle))

# Additional test cases
r1 = Rectangle(1, 4)
print(r1.area())

r2 = Rectangle(1411, 781)
print(r2.area())

r3 = Rectangle(5, 5)
print(r3.area())