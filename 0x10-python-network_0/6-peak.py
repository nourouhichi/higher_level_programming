#!/usr/bin/python3
"""
finding peak module
"""


def find_peak(list_of_integers):
    """ finding peak function"""
    if list_of_integers is None or len(list_of_integers) == 0:
       return None
    return max(list_of_integers)
