#!/usr/bin/python3
"""
This module defines the Rectangle class
with width and height fields.
"""


class Rectangle:
    """
    The definition of a class of type Rectangle with private
    variables width and height, and methods that returns the
    area and perimeter of the rectangle instance.
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
        """
        calculates and returns the perimeter of the rectangle
        Returns 0 if either the width or height private instance
        variable is 0
        """
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
