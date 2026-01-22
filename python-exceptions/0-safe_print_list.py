#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    for x in my_list:
        counter = counter + x
        try:
            print("{}".format(x), end="")
        except TypeError:
            print("chaîne de format non prise en charge transmise à NoneType")
    print()
    return counter
