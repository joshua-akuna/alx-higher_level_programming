#!/usr/bin/python3
"""This module defines the matrix_divided funtion"""

def matrix_divided(matrix, div):
    """The matrix_divided function divides each integer/float element
        of the matrix argument by the div argument.

        >>> matrix_divided([[1, 2, 3], [4, 5, 6]], 3)
        [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
    """
    type_err = "matrix must be a matrix (list of lists) of integers/floats"
    size_err = "Each row of the matrix must have the same size"

    if type(matrix) is not list or len(matrix) < 1:
        raise TypeError(type_err)


    for row in matrix:
        if type(row) is not list:
            raise TypeError(type_err)
        for item in row:
            if type(item) is not int and type(item) is not float:
                raise TypeError(type_err)
    
    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError(size_err)

    if type(div) is not float and type(div) is not int:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_matrix.append([round(item/div, 2) for item in row])

    return new_matrix
