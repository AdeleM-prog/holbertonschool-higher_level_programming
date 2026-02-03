#!/usr/bin/python3
"""no module imported"""


class BaseGeometry:
    """
    Public instance method
    that raises an Exception with the message area()
    is not implemented
    Public instance method that validates value
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """ Instantiation with width and height
    width and height must be private.
    width and height must be positive integers,
    validated by integer_validator
    """
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__height * self.__width

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
