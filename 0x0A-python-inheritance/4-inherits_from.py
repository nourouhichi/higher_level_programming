#!/usr/bin/python3
"""
module 1
"""


def inherits_from(obj, a_class):
    """ class 1"""
    if issubclass(type(obj), a_class):
        if type(obj) is not a_class:
            return True
    return False
