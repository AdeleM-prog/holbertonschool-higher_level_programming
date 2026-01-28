#!/usr/bin/python3
"""no module included"""


class Square:
    """ a class square"""
    def __init__(self, size=0):
        self.size = size
    """property that calls a function like
    an attribute"""
    @property
    def size(self):
        return self.__size

    """raises type erreor when not an integer
    raises valueError if under
    Private instance attribute
    """
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
