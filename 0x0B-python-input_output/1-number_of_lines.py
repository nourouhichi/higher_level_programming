#!/usr/bin/python3
"""
module 1
"""


def number_of_lines(filename=""):
    """function 1"""
    counter = 0
    with open(filename, 'r') as file:
        for line in file:
            counter += 1
    return counter
