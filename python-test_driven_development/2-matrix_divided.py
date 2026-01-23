#!/usr/bin/python3
""" This module provides a function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """matrix must be a list of lists of integers or floats,
    otherwise raise a TypeError.
    Each row of matrix must be of the same size, otherwise raise a TypeError
    div must be a number (integer or float), otherwise raise a TypeError
    div can’t be equal 0 otherwise raise ZeroDivisionError
    All elements of the matrix should be divided by div,
    rounded to 2 decimal places
    Returns a new matrix"""
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if (
        not isinstance(matrix, (list))
        or matrix == []
        or any(not isinstance(line, list) for line in matrix)
    ):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
            )

    line_len = None
    for line in matrix:
        if line == []:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )
        if line_len is None:
            line_len = len(line)
        elif len(line) != line_len:
            raise TypeError("Each row of the matrix must have the same size")

    for x in line:
        if not isinstance(x, (int, float)):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )

    new_matrix = []
    for line in matrix:
        new_line = [round(x / div, 2) for x in line]
        new_matrix.append(new_line)
    return new_matrix
