#!/usr/bin/python3
for x in range(99):
    if x // 10 % 10 < x %10 and x != 89:
        print("{:02d}, ".format(x), end=" ")
    elif x == 89:
        print(x)
