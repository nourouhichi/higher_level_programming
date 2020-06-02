#!/usr/bin/python3
""" module 1 """


class BaseGeometry:
    """class 1"""
    def area(self):
        """function 1"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """function 2"""
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
