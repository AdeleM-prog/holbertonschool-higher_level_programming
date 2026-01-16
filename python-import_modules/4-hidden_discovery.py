#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    names_list = dir(hidden_4)
    names_list = sorted(names_list)
    for line in names_list:
        if line.startswith("__") == False:
                print("{}".format(line))
