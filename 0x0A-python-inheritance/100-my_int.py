#!/usr/bin/python3

"""The module defines the MyInt class"""


class MyInt(int):
    """Definition for the MyInt class that inherits the int class
    and inverts the == and != operators
    """
    def __ne__(self, other):
        """inverts the not equal operator"""
        return super().__eq__(other)

    def __eq__(self, other):
        """inverts the equal operator"""
        return super().__ne__(other)
