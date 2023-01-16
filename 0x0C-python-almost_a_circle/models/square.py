#!/usr/bin/python3
"""
"Almost a circle" module
"""
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Define the Square class as a subclass of Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        """
#        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        define special __str__ method for printing a square
        (from instance call)
        """
        return '[Square] ({}) {}/{} - {}'.format(self.id,
                                                 self.x, self.y,
                                                 self.size)

    @property
    def size(self):
        """
        getter for size, retrieves size value
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        setter for size, validates the size value assignement
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        function that assigns an argument to each attribute
        """
        a_list = ["id", "size", "x", "y"]
        if args is not None and len(args) > 0 and len(args) <= 5:
            for i, arg in enumerate(args):
                setattr(self, a_list[i], arg)
        if kwargs is not None and len(kwargs) > 0 and len(kwargs) <= 5:
            for name, value in kwargs.items():
                setattr(self, name, value)

    def to_dictionary(self):
        """
        that returns the dictionary representation of a Square
        object/instance
        """
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
