#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""
module 1
"""


class Square(Rectangle):
    """ class 1"""
    def __init__(self, size):
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size
