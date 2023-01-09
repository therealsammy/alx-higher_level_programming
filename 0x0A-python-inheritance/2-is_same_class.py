#!/usr/bin/python3
"""
is_same_class module
"""


def is_same_class(obj, a_class):
    """
    function that returns True if the object is exactly an instance
    of the specified class ; otherwise False
    """
#    if dir(obj) == dir(a_class):
    if obj.__class__ == a_class:
        return True
    return False
