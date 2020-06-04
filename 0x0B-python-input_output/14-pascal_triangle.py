#!/usr/bin/python3
"""
module 1
"""


def pascal_triangle(n):
    """function 1"""
    listy = []
    if n <= 0:
        return listy
    for i in range(n):
        listy.append([])
        listy[i].append(1)
        for j in range(1, i):
            listy[i].append(listy[i-1][j-1] + listy[i-1][j])
        if i != 0:
            listy[i].append(1)
    return listy
