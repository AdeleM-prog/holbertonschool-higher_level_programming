#!/usr/bin/python3
"""This module provides a function that adds two numbers as integers."""


def add_integer(a, b=98):
    """Return the integer addition of a and b after validating their types.
    TypeErrors raised if needed.
    Numbers casted into integers if they are floats"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
