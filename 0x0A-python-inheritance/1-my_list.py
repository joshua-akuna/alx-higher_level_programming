#!/usr/bin/python3
"""The module defines the MyList class, a subtype of list"""


class MyList(list):
    """The MyList class defines the function print_sorted"""
    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))
