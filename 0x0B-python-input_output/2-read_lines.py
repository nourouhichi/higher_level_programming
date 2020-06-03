#!/usr/bin/python3
"""
module 1
"""


def read_lines(filename="", nb_lines=0):
    """function 1"""
    counter = 0
    with open(filename, 'r') as file:
        for line in file:
            counter += 1
            if nb_lines >= counter or nb_lines <= 0:
                print(line, end="")
