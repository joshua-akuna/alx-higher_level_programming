#!/usr/bin/python3
"""This module defines the LockedClass class"""


class LockedClass:
    """The LockedClass class witn no object or attribut
        that prevents the user from dynamically creating
        new instance attributes, except if the new class
        is called first_name
    """

    def __setattr__(self, name, value):
        """Defines the setettr magic function"""

        err = "'LockedClass' object has no attribute 'last_name'"
        if name == "first_name":
            self.__dict__[name] = value
        else:
            raise AttributeError(err)
