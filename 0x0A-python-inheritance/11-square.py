#!/usr/bin/python3
"""
module 1
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class 1"""
    def __init__(self, size):
        """function 1"""
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """function 2"""
        stri = "[Square] " + str(self.__size) + '/'
        stri += str(self.__size)
        return stri
