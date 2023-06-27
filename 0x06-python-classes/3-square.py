#!/usr/bin/python3
"""The definition of a Square class"""


class Square:
    """The constructor of the Square class
        that initializes the private instance property size"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    """The area method returns the area = size * size of the
        a Square instance"""
    def area(self):
        return (self.__size ** 2)
