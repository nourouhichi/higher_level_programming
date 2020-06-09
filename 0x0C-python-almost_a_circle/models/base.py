#!/usr/bin/python3
"""
module 1
"""


class Base:
    """class 1"""
    __nb_objects = 0

    def __init__(self, id=None):
        """function 1"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
