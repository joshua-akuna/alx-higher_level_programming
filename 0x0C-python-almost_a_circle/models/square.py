#!/usr/bin/python
"""The square model defines the Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    The definition for the Square sub class with
    properties size, x, y and id.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """constructor for the initialization of Square instances"""
        super().__init__(size, size, x, y, id)
    
    def update(self, *args, **kwargs):
        """
        This funtion is used to update the properties of
        Square instances
        """
        if args:
            arr = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                setattr(self, arr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    @property
    def size(self):
        """getter for the size property"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for the size property"""
        self.width = value
        self.height = value

    def to_dictionary(self):
        """returns the dictionary representation of the current
        Square instance."""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
