#!/usr/bin/python3
"""This module contains the add_integer function.
    Below is an interactive example in a documenation for doctest.
    >>> add_integer(5, -3)
    2
"""


def add_integer(a, b=98):
    """Definition for a add_integer function that returns the sum
        its arguments.
    """
    if not isinstance(a, int) and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
