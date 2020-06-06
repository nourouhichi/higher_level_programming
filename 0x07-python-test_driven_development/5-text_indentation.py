#!/usr/bin/python3
"""
module 1
"""


def text_indentation(text):
    """function 1"""
    test = False
    if type(text) is not str:
        raise TypeError("text must be a string")
    for char in text:
        if char is "?" or char is "." or char is ":":
            print(char, end="")
            print('\n')
            test = True
        else:
            if test is True:
                pass
            else:
                print(char, end="")
            test = False
