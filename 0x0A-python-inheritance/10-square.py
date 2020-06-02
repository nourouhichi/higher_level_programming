#!/usr/bin/python3
"""
module 1 
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class 1"""
    def __init__(self, size):
        """function 1"""
        size = super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """function 2"""
        return self.__size * self.__size

    def __str__(self):
        """function 3"""
        stri = "[Rectangle] "
        stri += str(self.__size) + '/' + str(self.__size)
        return stri
