#!/usr/bin/python3
"""This module defines the LockedClass class"""


class LockedClass:
    """The LockedClass class witn no object or attribut
        that prevents the user from dynamically creating
        new instance attributes, except if the new class
        is called first_name
    """
    __slots__ = ("first_name")

    def __setattr__(self, name, value):
        err = "'LockedClass' object has no attribue 'last_name'"
        
        if not hasattr(self, name) and name != 'first_name':
            raise AttributeError(err)
        super().__setattr__(name, value)
