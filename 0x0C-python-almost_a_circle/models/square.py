#!/usr/bin/python3
"""
module 1
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class 1"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if args:
            for i, j in enumerate(args):
                if i is 0:
                    self.id = j
                elif i is 1:
                    self.size = j
                elif i is 2:
                    self.x = j
                elif i is 3:
                    self.y = j
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
