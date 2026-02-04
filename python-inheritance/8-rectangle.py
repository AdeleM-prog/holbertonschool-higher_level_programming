#!/usr/bin/python3

"""
This module defines the class Rectangle.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class initiating a rectangle
    """

    def __init__(self, width, height):
        """
        Instantiation with width and height
        width and height must be private.
        width and height must be positive integers,
        validated by integer_validator
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
