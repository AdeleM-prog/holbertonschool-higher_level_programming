#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for element in i:
            print("{:d}".format(element), end=" ")
        print()
