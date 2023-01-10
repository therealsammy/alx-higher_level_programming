#!/usr/bin/python3
"""
9-add_item module
"""

import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


def add_items():
    """
    function that adds all arguments to a Python list
    and then saves them to a file
    """
    try:
        python_list = load_from_json_file('add_item.json')
    except:
        python_list = []

    for i in range(1, len(sys.argv)):
        python_list.append(sys.argv[i])

    save_to_json_file(python_list, 'add_item.json')

if __name__ == '__main__':
    add_items()
