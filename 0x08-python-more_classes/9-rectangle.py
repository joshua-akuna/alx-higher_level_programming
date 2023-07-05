#!/usr/bin/python3
"""
This module defines the Rectangle class
with width and height fields.
"""


class Rectangle:
    """
    The definition of a class of type Rectangle with the
    following members
    1. private instance variables width and height
    2. a public class variable number_of_instances that stores
        the current numbers of Rectangle objects and the
        print_symbol class variable.
    3. methods for area and perimeter
    4. overloaded str, repr and del magic methods
    Test 1
    >>> print(Rectangle(2, 4).__dict__)
    {'_Rectangle__width': 2, '_Rectangle__height': 4}

    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        A constructor for the Rectangle class that initializes the
        width and height fields and increments the value of the
        number_of_instances class variable by a value of 1
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    def area(self):
        """ calculates and returns the area of the rectangle """
        return self.width * self.height

    def perimeter(self):
        """ calculates and returns the perimeter of the rectangle """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns rect_2 if it is bigger than rect_1 else returns rect_1"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_2 if rect_2.area() > rect_1.area() else rect_1

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance of width == height == size"""
        return cls(size, size)

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
            for j in range(self.width):
                res += f"{self.print_symbol}"
        return res

    def __repr__(self):
        """
        Returns a string representation of a rectangle instance to
        be able to recreate a new instance by using eval
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """
        prints the string below when an instance of a Rectangle is
        deleted and decrements the number_of_instances class variable
        by a value of 1
        """
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1
