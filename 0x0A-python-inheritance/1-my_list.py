#!/usr/bin/python3
"""
module 1
"""


class MyList(list):
    """class 1 """
    def print_sorted(self):
        """function 1"""
        print(sorted(self))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/1-my_list.txt")
