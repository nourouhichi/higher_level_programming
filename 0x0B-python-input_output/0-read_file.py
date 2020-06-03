#!/usr/bin/python3
"""
module 1
"""


def read_file(filename=""):
    """ function 1"""
    with open(filename, 'r') as file:
        reading = file.read()
    print(reading, end="")
