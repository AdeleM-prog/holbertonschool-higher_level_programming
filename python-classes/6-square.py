#!/usr/bin/python3
"""no module included"""


class Square:
    """
    a class Square that defines a square by
    Private instance attribute size
    Private instance attribute position
    Instantiation with optional size and optional position
    Public instance method area that returns the square area
    Public instance method my_print that prints the square with the character #
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializing square
        Arguments: size (size of the square)
        position (tuple of 2 int for the position of the square)
        Instantiation with optional size and optional position
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Method that reads the attribute __size (private)
        and returns it
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
