#!/usr/bin/python3
"""no module included"""


class Square:
    """ a class square"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
    @property
    def size(self):
        """
        property that calls a function like
        an attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        raises type erreor when not an integer
        raises valueError if under
        Private instance attribute
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        """Private instance attribute"""
        self.__size = value

    @property
    def position(self):
        """
        property that calls a function like
        an attribute
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        raises type erreor when not an integer
        raises valueError if under
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """
        Public instance method that returns the square area
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Public instance method that prints in stdout the square
        with the character #
        """
        if self.size == 0:
            print()
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="")
            print()
