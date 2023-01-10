#!/usr/bin/python3
"""
2-read_lines module
"""


def read_lines(filename="", nb_lines=0):
    """
    function that reads n lines of a text file (UTF8) and prints it to stdout
    """
    with open(filename, 'r') as f:
        if nb_lines > 0:
            for i in range(nb_lines):
                print(f.readline(), end='')
        else:
            print(f.read(), end='')
