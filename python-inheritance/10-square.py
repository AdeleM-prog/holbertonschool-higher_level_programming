#!/usr/bin/python3

"""
module initializing a square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a class Square that inherits from Rectangle
    Instantiation with size
    size must be private
    size must be a positive integer, validated by integer_validator
    the area() method must be implemented
    print() should print, and str() should return, the square description
    """

    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return self.__size * self.__size
