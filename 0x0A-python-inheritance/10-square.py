#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""
module 1
"""


class Square(Rectangle):
    """ class 1"""
    def __init__(self, size):
        size = super().integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        stri = "[Rectangle] "
        stri += str(self.__size) + '/' + str(self.__size)
        return stri
