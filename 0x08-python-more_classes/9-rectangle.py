#!/usr/bin/python3
""""
rectangle module
"""


class Rectangle:
    """
    rectangle class
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if (self.__width * self.__height) is 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        rect = ""

        if self.__height * self.__width is 0:
            return rect
        for i in range(self.__height - 1):
            rect += str(self.print_symbol) * self.__width + "\n"
        rect += str(self.print_symbol) * self.__width
        return rect

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(slef):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if (rect_1.area() >= rect_2.area()):
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """returns a new instance of type Rectangle"""
        return cls(size, size)
