#!/usr/bin/python3
"""square module"""


class Square:
    """class Square"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        y = type(value) is not tuple
        x = type(value[0]) is not int
        i = type(value[1]) is not int
        z = value[0] < 0
        v = value[1] < 0
        if y or x or i or z or v:
            raise TypeError("position must be a tuple of 2 positive integer")
        else:
            self.__position = value

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size is 0:
            print()

        else:
            print('\n' * self.__position[1], end="")
            for i in range(self.__size):
                print(' ' * self.__position[0], end="")
                print('#' * self.__size)
