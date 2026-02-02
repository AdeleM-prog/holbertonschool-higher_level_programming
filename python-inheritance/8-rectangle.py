#!/usr/bin/python3
"""no module imported"""


class Rectangle:
    """
    Instantiation with width and height:
    width and height must be private
    width and height must be positive integers, validated by integer_validator
    Public instance method
    that raises an Exception with the message area()
    is not implemented
    Public instance method that validates value
    """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
