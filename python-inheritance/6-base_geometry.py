#!/usr/bin/python3
"""no module imported"""


class BaseGeometry:
    """Public instance method
    that raises an Exception with the message area()
    is not implemented"""
    def area(self):
        raise Exception("area() is not implemented")
