#!/usr/bin/python3
"""The module defines a BaseGeometry class"""


class BaseGeometry():
    """The BaseGeometry class defines a single area function that
    raises with the message 'area() is not implemented'
    """

    def area(self):
        """raises an Exception with the message 'area() is not implemented'"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates the value argument, you can assume name is always string
        """
        # raise a TypeError if value is not an integer
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        # raises a ValueError if value is greater than or less than 0
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
