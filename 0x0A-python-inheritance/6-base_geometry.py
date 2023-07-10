#!/usr/bin/python3
"""The module defines a BaseGeometry class"""


class BaseGeometry():
    """The BaseGeometry class defines a single area function that
    raises with the message 'area() is not implemented'
    """

    def area(self):
        """raises an Exception with the message 'area() is not implemented'"""
        raise Exception("area() is not implemented")
