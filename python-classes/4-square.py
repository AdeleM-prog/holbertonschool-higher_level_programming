#!/usr/bin/python3
"""a class Square that defines a square"""


class Square:
    def __init__(self, size=0):
        self.size = size
        """raises type erreor when not an integer
        raises valueError if under
        Private instance attribute
        """
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        """Private instance attribute"""
        self.__size = value

    """Public instance method
    that returns the current square area"""
    def area(self):
        return self.__size * self.__size
