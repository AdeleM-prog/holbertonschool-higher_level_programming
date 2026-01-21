#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for idx, element in enumerate(i):
            if idx != 0:
                print(" ", end="")
            print("{:d}".format(element), end="")
        print()
