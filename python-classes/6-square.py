#!/usr/bin/python3
"""no module included"""


class Square:
    """ a class square"""
    def __init__(self, size=0, position=(0, 0)):
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

    """method position gives an attribute position"""
    def position(self):
        self.position = position

    """property that calls a function like
    an attribute"""
    @property
    def position(self):
        return self.__position

    """raises type erreor when not an integer
    raises valueError if under
    """
    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")

    """Public instance method
    that returns the current square area"""
    def area(self):
        return self.__size * self.__size

    """Public instance method
    that prints in stdout the square
    with the character #"""
    def my_print(self):
        if self.size == 0:
            print()
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="")
            print()
