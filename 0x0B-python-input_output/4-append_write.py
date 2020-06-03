#!/usr/bin/python3
"""
module 1
"""


def append_write(filename="", text=""):
    """function1 """
    with open(filename, 'a') as file:
        appending = file.write(text)
    return len(text)
