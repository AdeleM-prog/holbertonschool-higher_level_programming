#!/usr/bin/python3
""" no module included"""


class Rectangle:
    """
    a class Square that defines a rectangle by
    Private instance attribute width
    Private instance attribute height
    Instantiation with optional width and optional height
    """
    def __init__(self, width=0, height=0):
        """
        Initializing rectangle
        Arguments: width (width of the rectangle)
        height (height of the rectangle)
        Instantiation with optional width and optional height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Method that reads the attribute __width (private)
        and returns it
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Method that modifies the private attribute
        raises TypeError when not an integer
        raises valueError if under 0
        Private instance attribute
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Method that reads the attribute __height (private)
        and returns it
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Method that modifies the private attribute
        raises TypeError when not an integer
        raises valueError if under 0
        Private instance attribute
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Public instance method
        that returns the current rectangle area
        """
        return self.__width * self.__height

    def perimeter(self):
        """ Public instance method
        that returns the current rectangle perimeter
        """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (self.width + self.height) * 2

    def __str__(self):
        """ Public instance method
        that returns the string of the current rectangle
        """
        if self.width == 0 or self.height == 0:
            return ""
        else:
            return (("#" * self.width + "\n") * self.height)[:-1]

    def __repr__(self):
        """ Public instance method
        that returns a string representation of the rectangle
        """
        return "Rectangle({}, {})".format(self.width, self.height)
