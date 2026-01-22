#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    for i in range(x):
        try:
            counter = counter + 1
            print("{}".format(my_list[i]), end="")
        except (IndexError):
            counter = counter - 1
            break
    print()
    return counter
