#!/usr/bin/python3
"""The module defines a Rectangle class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines the Square class"""

    def __init__(self, size):
        """A constructor for the Square class"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
