#!/usr/bin/python3
""" This module contains the is_kind_of_class function """


def is_kind_of_class(obj, a_class):
    """returns True if the object is an of or if the object is
    an instance of a class that inherited from a_class Base class
    """
    return isinstance(obj, a_class)
