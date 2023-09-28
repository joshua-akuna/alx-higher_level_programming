#!/usr/bin/python3
""" The module defines the find_peak function """

def find_peak(list_of_integers):
    """ The function defines an algorithm that finds a peak in
    a list of unsorted integers with the lowest complexity
    """
    if not list_of_integers or len(list_of_integers) == 0:
        return None

    left, right = 0, len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return list_of_integers[left]
