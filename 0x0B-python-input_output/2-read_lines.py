#!/usr/bin/python3
"""
module 1
"""


def read_lines(filename="", nb_lines=0):
    """function 1"""
    counter = 0
    lines = ""
    with open(filename, 'r') as file:
        if nb_lines == 0:
            reading = file.read()
            print(reading, end="")
            return
        for line in file:
            if counter == nb_lines:
                print(lines, end="")
                return
            lines += str(line)
            counter += 1
