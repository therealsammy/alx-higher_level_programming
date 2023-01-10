#!/usr/bin/python3
"""
3-write_file module
"""


def write_file(filename="", text=""):
    """
    function that writes a string to a text file (UTF8)
    and returns the number of characters written
    """
    with open(filename, 'w') as wf:
        return wf.write(str(text))
#    with open(filename, 'r') as rf:
#        rf.read()
#        return(rf.tell())
