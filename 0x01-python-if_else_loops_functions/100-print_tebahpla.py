#!/usr/bin/python3
x = 0
for ascii in range(122, 96, -1):
    x = x + 1
    if x % 2 == 1:
        print("{:c}".format(ascii), end="")
    else:
        print("{:c}".format(ascii - 32), end="")
