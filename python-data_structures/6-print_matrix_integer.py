#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for element in i:
            print("{}".format(element), end=" ")
        print()
