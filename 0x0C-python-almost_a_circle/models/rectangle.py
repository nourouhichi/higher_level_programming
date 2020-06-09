#!/usr/bin/python3
"""
module 1
"""
from models.base import Base


class Rectangle(Base):
    """class 1 """
    def __init__(self, width, height, x=0, y=0, id=None):
        """function 1"""
        Base.__init__(self, id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """function 2"""
        return self.__width

    @width.setter
    def width(self, value):
        """function 3"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """function"""
        return self.__height

    @height.setter
    def height(self, value):
        """function 4 """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """function 5"""
        return self.__x

    @x.setter
    def x(self, value):
        """function 6"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """function 7"""
        return self.__y

    @y.setter
    def y(self, value):
        """function 8"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """function 9"""
        return self.__height * self.__width

    def display(self):
        """function 10"""
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(' ' * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """function 11"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format
    (self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """function 12"""
        if args:
            args_list = enumerate(args)
            for i, j in args_list:
                if i is 0:
                    self.id = j
                elif i is 1:
                    self.__width = j
                elif i is 2:
                    self.__height = j
                elif i is 3:
                    self.__x = j
                elif i is 4:
                    self.__y = j
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """function 13"""
        return {'id': self.id, 'width': self.width,
                'height': self.height, 'x': self.x, 'y': self.y}
