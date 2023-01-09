#!/usr/bin/python3
"""
is add_attribute module
"""


def add_attribute(obj, a, v):
        """function that adds a new attribute to an object if it’s possible """
    res = getattr(obj, "__doc__", None)
    if res is None:
        setattr(obj, a, v)
    else:
        raise TypeError("can't add new attribute")