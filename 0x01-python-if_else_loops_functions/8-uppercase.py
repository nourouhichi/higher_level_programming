#!/usr/bin/python3
def uppercase(str):
    for x in str:
        if 96 < ord(x) < 123:
            upp = ord(x) - 32
        else:
            upp = ord(x)
        print("{:c}".format(upp), end="")
    else:
        print()
