#!/usr/bin/python3
"""
100-append_after module
"""


def append_after(filename="", search_string="", new_string=""):
    """
    function that inserts a line of text to a file,
    after each line containing a specific string
    """
    with open(filename, 'r') as f:
        a_list = f.readlines()
        b_list = a_list.copy()
        j = 0
        for i in range(len(a_list)):
            if search_string in a_list[i]:
                b_list.insert(j + 1, new_string)
                j += 1
#                print(a_list)
#                print(b_list)
            j += 1
    with open(filename, 'w') as wf:
        for i in range(len(b_list)):
            wf.write(b_list[i])
