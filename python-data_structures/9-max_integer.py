#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    else:
        val_max = my_list[0]
        for i in my_list:
            if i > val_max:
                val_max = i
    return val_max
