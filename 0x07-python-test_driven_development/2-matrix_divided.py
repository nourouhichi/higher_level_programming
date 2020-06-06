#!/usr/bin/python3
"""
2-matrix_divided
"""


def matrix_divided(matrix, div):
    """
    matrix_divided  function
    """
    x = 0
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix \
                (list of lists) of integers/floats")
    for i in range(len(matrix)):
        if type(matrix[i]) is not list:
            raise TypeError("matrix must be a \
                    matrix (list of lists) of integers/floats")
    for i in matrix:
        for j in i:
            if type(j) is not float and type(j) is not int:
                raise TypeError("matrix must be a matrix \
                    (list of lists) of integers/floats")
    for z in range(len(matrix[0])):
        x += 1
    for j in range(1, len(matrix)):
        if len(matrix[j]) is not x:
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div is 0:
        raise ZeroDivisionError("division by zero")
    return[[round(j / div, 2) for j in i] for i in matrix]
