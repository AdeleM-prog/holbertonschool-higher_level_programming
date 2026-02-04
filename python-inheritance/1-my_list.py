#!/usr/bin/python3
"""
This module defines a class that prints list behavior
with a sorted method
"""


class MyList(list):
    """ a class MyList that inherits the class list"""

    def print_sorted(self):
        """
        Public instance method that prints the list,
        but sorted (ascending sort)
        """
        print(sorted(self))
