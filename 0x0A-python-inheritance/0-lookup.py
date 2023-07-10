#!/usr/bin/python3
"""This module contains the lookup function"""


def lookup(obj):
    """The lookup function returns the list of available attributes
        and methods of an object.
    """
    return dir(obj)
