#!/usr/bin/python3
"""The module contains the max_integer function"""


def max_integer(list1=[]):
    """
    Finds and returns the maximum integer in a list argument.
    If the list is empty, the function returns None.
    """
    if len(list1) == 0:
        return None

    result = list1[0]
    i = 1
    while i < len(list1):
        if list1[i] > result:
            result = list1[i]
        i += 1
    return result
