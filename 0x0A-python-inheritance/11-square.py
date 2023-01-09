#!/usr/bin/python3
"""
BaseGeometry module
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle

# class BaseGeometry:
#     """
#     empty class
#     """

#     def area(self):
#         """raises an Exception"""
#         raise Exception('area() is not implemented')

#     def integer_validator(self, name, value):
#         """method that validates value"""
#         if not isinstance(value, int) or isinstance(value, bool):
#             raise TypeError('{} must be an integer'.format(name))
#         if value <= 0:
#             raise ValueError('{} must be greater than 0'.format(name))


# class Rectangle(BaseGeometry):
#     """
#     class Rectangle that inherits from BaseGeometry
#     """

#     def __init__(self, width, height):
#         """initializes variables and methods"""
#         self.__width = width
#         self.__height = height
#         self.integer_validator("width", self.__width)
#         self.integer_validator("height", self.__height)

#     def area(self):
#         """function that returns the area"""
#         return self.__width * self.__height

#     def __str__(self):
#         """prints a string representation of the Rectangle instance"""
#         return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """
    class Square that inherits from Rectangle
    """

    def __init__(self, size):
        """initializes variables and methods"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """prints a string representation of the Square instance"""
        return "[Square] {}/{}".format(self.__size, self.__size)
