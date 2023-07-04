#!/usr/bin/python3
"""This module defines the LockedClass class"""


class LockedClass:
    """The LockedClass class witn no object or attribut
        that prevents the user from dynamically creating
        new instance attributes, except if the new class
        is called first_name
    """
    __slots__ = ('first_name',)

    def __setattr__(self, name, value):
        """setattr magic method"""
        err = "'LockedClass' object has no attribute '{}'"
        if not hasattr(self, 'first_name') and name != 'first_name':
            raise AttributeError(err.format(name))
        super().__setattr__(name, value)
