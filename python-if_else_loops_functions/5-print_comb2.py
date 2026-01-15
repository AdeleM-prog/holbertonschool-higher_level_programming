#!/usr/bin/python3
for i in range(00, 100):
    if i <= 98:
        print("{:02d}".format(i), end=", ")
    elif i == 99:
        print("{:d}".format(i))
