#!/usr/bin/python3
"""a class Square that defines a square"""


class Square:
    """ a class square"""
    def __init__(self, size=0):
        """raises type erreor when not an integer
        raises valueError if under
        Private instance attribute
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Public instance method
        that returns the current square area"""
        return self.__size * self.__size
