#!/usr/bin/python3
"""
The module 100-matrix_mul contains the matrix_mul and the
mult_row_by_col functions that returns the product of two
2-D list arguments.

>>> matrix_mul([[1, 2]], [[3, 4], [5, 6]])
[[13, 16]]
"""


def matrix_mul(m_a, m_b):
    """
    The function returns the product of 2 valid matrices
    >>> matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]])
    [[7, 10], [15, 22]]
    """

    # checks if both arguments are lists
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    # checks if the list arguments are empty or contain empty list
    if len(m_a) < 1:
        raise ValueError("m_a can't be empty")
    if len(m_b) < 1:
        raise ValueError("m_b can't be empty")

    # checks if the list arguments are empty or contain empty list
    if type(m_a[0]) is list and len(m_a[0]) < 1:
        raise ValueError("m_a can't be empty")
    if type(m_b[0]) is list and len(m_b[0]) < 1:
        raise ValueError("m_b can't be empty")

    # checks to validate that both list arguments contains only lists
    for row in m_a:
        if type(row) is not list:
            raise TypeError("m_a must be a list of lists")
    for row in m_b:
        if type(row) is not list:
            raise TypeError("m_b must be a list of lists")

    # checks that both arguments are list of lists of integers or floats
    for row in m_a:
        for item in row:
            if type(item) is not float and type(item) is not int:
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for item in row:
            if type(item) is not float and type(item) is not int:
                raise TypeError("m_b should contain only integers or floats")

    # checks that the size of the list arguments is uniform (a quadrilateral)
    size = len(m_a[0])
    for row in m_a:
        if len(row) != size:
            raise TypeError('each row of m_a must be of the same size')
    size = len(m_b[0])
    for row in m_b:
        if len(row) != size:
            raise TypeError('each row of m_b must be of the same size')

    # dimensions of m_a and m_b
    row_a = len(m_a)
    col_a = len(m_a[0])
    row_b = len(m_b)
    col_b = len(m_b[0])

    # checks if m_a can be multiplied by m_b
    if col_a != row_b:
        raise ValueError("m_a and m_b can't be multiplied")

    # multiples m_a by m_b
    new_mat = []
    for i in range(row_a):
        new_row = []
        row = m_a[i]
        for j in range(col_b):
            col = [item[j] for item in m_b]
            res = mult_row_by_col(row, col)
            new_row.append(res)
        new_mat.append(new_row)
    return (new_mat)


def mult_row_by_col(row, col):
    """
    returns the sum of the product of the elements in the
    corresponding index of the row and col arguments
    """
    res = 0
    for i in range(len(row)):
        res += row[i] * col[i]
    # returns the sum
    return res
