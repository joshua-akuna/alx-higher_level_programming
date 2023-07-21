#!/usr/bin/python3
"""
This module defines the Rectangle sub class which
inherits the Base super class
"""
from models.base import Base


class Rectangle(Base):
    """
    The Rectangle class with public instance properties
    width, height, x, y and id.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """This constructor initializes a Rectangle instance"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def area(self):
        """The area function returns the area of the rectangle"""
        return self.height * self.width

    def display(self):
        """The display property displays the rectangle using #'s"""
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(' ' * self.x, end='')
            print('#' * self.width)

    def update(self, *args, **kwargs):
        """
        The update property is used to update the properties of
        a rectangle instance.
        """
        size = len(args)
        if size > 0:
            self.id = args[0]
        if size > 1:
            self.width = args[1]
        if size > 2:
            self.height = args[2]
        if size > 3:
            self.x = args[3]
        if size > 4:
            self.y = args[4]

        if size == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        This function returns the dictionary representation
        of the current rectangle instnace.
        """
        return {
            'y': self.y,
            'x': self.x,
            'id': self.id,
            'width': self.width,
            'height': self.height
        }

    def __str__(self):
        """
        This function returns a string representation of the
        the current rectangle instance.
        """
        return "[{}] ({}) {}/{} - {}/{}".format(
            self.__class__.__name__,
            self.id,
            self.x,
            self.y,
            self.width,
            self.height
        )

    def __repr__(self):
        """
        returns the repr string representation of the current Rectangle
        instance.
        """
        return f"{self.id},{self.width},{self.height},{self.x},{self.y}"

    @property
    def width(self):
        """getter for the width property"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the width property"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """getter for the height property"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the width property"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """getter for the x property"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for the x property"""
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """getter for the y property"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for the y property"""
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value
