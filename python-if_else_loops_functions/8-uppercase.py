#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord('a') <= ord(i) <= ord('z'):
            i = ord(i) - 32
            print("{i}".format(i=chr(i)), end="")
        else:
            print(f"{i}", end="")
    print()
