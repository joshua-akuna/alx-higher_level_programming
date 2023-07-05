#!/usr/bin/python3
"""
This module defines the print_square function that prints a
square of "#'s" whose side is of length of argument size.
"""


def print_square(size):
    """
    The print_square function prints a square of #'s with each
    side of length of argument size.

    >>> print_square(1)
    #

    >>> print_square("5")
    Traceback (most recent call last):
        ...
    TypeError: size must be an integer

    >>> print_square(-1)
    Traceback (most recent call last):
        ...
    ValueError: size must be >= 0

    >>> print_square(0)
    <BLANKLINE>
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        print("#" * size)
