#!/usr/bin/python3
"""
11-student module
"""


class Student:
    """
    define the Student class
    """

    def __init__(self, first_name, last_name, age):
        """initialize variables and methods"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ """
        return self.__dict__
