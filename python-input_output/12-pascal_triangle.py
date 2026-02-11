#!/usr/bin/python3
"""
this module implements a function reprensenting the Pascal's triangle of n:
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
"""


def pascal_triangle(n):
    """
    function returns a list of lists of integers
    representing the Pascal triangle of n
    """
    triangle = []
    if n > 0:
        for row in range(n):
            line = [1] * (row + 1)
            for column in range(row):
                if 1 <= column:
                    line[column] = (
                        triangle[row - 1][column - 1]
                        + triangle[row - 1][column]
                    )
            triangle.append(line)
    return triangle
