#!/usr/bin/python3
"""The module contains the is_same_class function"""


def is_same_class(obj, a_class):
    """ returns True if obj is an instance of a_class; otherwise False"""
    return type(obj) is a_class
