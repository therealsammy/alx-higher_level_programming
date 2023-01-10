#!/usr/bin/python3
"""
1-number_of_lines module
"""


def number_of_lines(filename=""):
    """function that returns the number of lines of a text file"""
    with open(filename, 'r') as f:
        return len(f.readlines())
