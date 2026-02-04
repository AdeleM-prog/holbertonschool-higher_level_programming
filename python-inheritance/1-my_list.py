#!/usr/bin/python3
""" no module added"""


class MyList(list):
    """ a class MyList that inherits the class list"""

    def print_sorted(self):
        """
        Public instance method that prints the list,
        but sorted (ascending sort)
        """
        print(sorted(self))
