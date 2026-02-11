#!/usr/bin/python3
""" This module provides a function that writes a string to a
text file (UTF8) and returns the number of characters written
"""


def write_file(filename="", text=""):
    """ function that writes a string to a text file (UTF8)
    returns the number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        nb = f.write(text)
        return nb
