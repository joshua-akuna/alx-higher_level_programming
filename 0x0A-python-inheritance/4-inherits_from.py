#!/usr/bin/python3
""" This module contains the inherits_from function """


def inherits_from(obj, a_class):
    """returns True if argument obj is an instance of a class that
    inherited (directly or indirectly) from the specified class,
    otherwise False
    """
    return isinstance(obj, a_class)
