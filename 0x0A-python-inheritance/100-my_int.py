#!/usr/bin/python3
"""
module 1
"""


class MyInt(int):
    """ class 1"""
    def __eq__(self, x):
        """function 1"""
        return int(self) != int(x)

    def __ne__(self, y):
        """function 2"""
        return int(self) == int(y)
