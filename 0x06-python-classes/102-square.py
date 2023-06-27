#!/usr/bin/python3
"""Definition for the Square class"""


class Square:
    """Defines the constructor for the Square class the initializes
        the private instance property of the instance (self)"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    """Defines the getter for the private instance self property"""
    @property
    def size(self):
        return self.__size

    """Defines the setter for the private instance self property"""
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """overloads the magic method (dunders) for equality"""
    def __eq__(self, other):
        return self.size == other.size

    """overloads the magic method (dunders) for less than"""
    def __lt__(self, other):
        return self.size < other.size

    """overloads the magic method (dunders) for greater than"""
    def __gt__(self, other):
        return self.size > other.size

    """overloads the magic method (dunders) for greater than or equal to"""
    def __ge__(self, other):
        return self.size >= other.size

    """overloads the magic method (dunders) for less than or equal to"""
    def __le__(self, other):
        return self.size <= other.size

    """overloads the magic method (dunders) for not equal to"""
    def __ne__(self, other):
        return self.size != other.size

    """The area method returns the area = size * size of the
        a Square instance"""
    def area(self):
        return (self.__size * self.__size)
