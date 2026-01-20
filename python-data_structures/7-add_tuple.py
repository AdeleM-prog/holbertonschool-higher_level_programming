#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    if len(tuple_a) >= 1:
        valuea_0 = tuple_a[0]
    else:
        valuea_0 = 0
    if len(tuple_a) >= 2:
        valuea_1 = tuple_a[1]
    else:
        valuea_1 = 0
    if len(tuple_b) >= 1:
        valueb_0 = tuple_b[0]
    else:
        valueb_0 = 0
    if len(tuple_b) >= 2:
        valueb_1 = tuple_b[1]
    else:
        valueb_1 = 0

    return valuea_0 + valueb_0, valuea_1 + valueb_1
