#!/usr/bin/python3
def multiply_by_2(my_dict):
    new_dict = {}
    for i, n in my_dict.items():
        new_dict[i] = n * 2
    return new_dict
