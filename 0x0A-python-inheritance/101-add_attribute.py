#!/usr/bin/python3

"""The module defines the add_attribute function"""


def add_attribute(obj, attr, value):
    """The add_attribute adds a new attribute to an object if possible"""

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
