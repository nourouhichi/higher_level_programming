#!/usr/bin/python3
"""
mudule 1
"""


class Student:
    """class 1"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        dic = {}
        for a in attrs:
            if a in self.__dict__:
                dic[a] = self.__dict__[a]
        return dic
