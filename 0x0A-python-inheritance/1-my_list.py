#!/usr/bin/python3
"""
class MyList that inherits from list
"""


class MyList(list):
    """
    Subclass that inherits from list
    """

    def print_sorted(self):
        """prints the list, but sorted"""
        return print(sorted(self))
