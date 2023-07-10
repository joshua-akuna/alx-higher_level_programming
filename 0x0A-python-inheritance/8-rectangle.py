#!/usr/bin/python3
"""The module defines a Rectangle class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """The BaseGeometry class defines a single area function that
    raises with the message 'area() is not implemented'
    """

    def __init__(self, width, height):
        """A constructor for the BaseGeometry class"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
