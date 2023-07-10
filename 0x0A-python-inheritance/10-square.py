#!/usr/bin/python3
"""The module defines a Rectangle class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines the Square class"""

    def __init__(self, size):
        """A constructor for the Square class"""
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Calculates the area of the Square object"""
        return self.__size * self.__size
