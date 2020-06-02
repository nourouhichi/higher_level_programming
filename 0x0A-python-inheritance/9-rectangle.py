#!/usr/bin/python3
"""
module 1
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ class 1"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        stri = "[Rectangle] "
        stri += str(self.__width) + '/' + str(self.__height)
        return stri

    def area(self):
        return self.__width * self.__height
