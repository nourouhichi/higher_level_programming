#!/usr/bin/python3
"""
module 1
"""


def write_file(filename="", text=""):
    """function1"""
    with open(filename, 'w') as file:
        writing = file.write(text)
    return len(text)
