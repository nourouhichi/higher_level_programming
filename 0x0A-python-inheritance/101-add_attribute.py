#!/usr/bin/python3
"""
module1
"""


def add_attribute(c, name, value):
    """function 1"""
    if not hasattr(c, '__dict__'):
        raise TypeError("can't add new attribute")
    else:
        setattr(c, name, value)
