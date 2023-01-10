#!/usr/bin/python3
"""
12-student module
"""


class Student:
    """
    Define the Student class
    """

    def __init__(self, first_name, last_name, age):
        """initialize variables and methods"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        function that retrieves a dictionary representation
        of a Student instance
        """
        if attrs is None:
            return self.__dict__
        else:
            a_dict = {}
            for attr, value in (self.__dict__).items():
                if attr in attrs:
                    a_dict[attr] = value
            return a_dict
