#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    y = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
        except (TypeError, ValueError):
            y = y + 1
    print()
    return x - y
