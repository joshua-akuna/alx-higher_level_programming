#!/usr/bin/python3
"""
This module defines the Rectangle class
with width and height fields.
"""


class Rectangle:
    """
    The definition of a class of type Rectangle with private
    instance variables width and height, methods for area and
    perimeter, and overloaded str magic method
    Test 1
    >>> print(Rectangle(2, 4).__dict__)
    {'_Rectangle__width': 2, '_Rectangle__height': 4}

    """
    def __init__(self, width=0, height=0):
        """
        A constructor for the Rectangle class that
        initializes the width and height fields.
        """
        self.height = height
        self.width = width

    def area(self):
        """ calculates and returns the area of the rectangle """
        return self.width * self.height

    def perimeter(self):
        """ calculates and returns the perimeter of the rectangle """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    @property
    def width(self):
        """ A getter for the width field """
        return self.__width

    @width.setter
    def width(self, value):
        """
        A setter for the width field.
        The width must be a positive integer
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ A getter for the height field """
        return self.__height

    @height.setter
    def height(self, value):
        """
        A setter for the height field.
        The height must be a positive integer
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def print(self):
        """
        prints the string representation of the
        current Rectangle instance
        """
        print(self.str)

    def __str__(self):
        """
        returns an informal representation of the current Rectangle
        instance as a string.
        """
        res = ""
        if self.height == 0 or self.width == 0:
            return res
        for i in range(self.height):
            if i:
                res += '\n'
            res += '#' * self.width
        return res

    def __repr__(self):
        """
        Returns a string representation of a rectangle instance to
        be able to recreate a new instance by using eval
        """
        return f"Rectangle({self.width}, {self.height})"
