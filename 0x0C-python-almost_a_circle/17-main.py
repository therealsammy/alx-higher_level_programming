#!/usr/bin/python3
""" 17-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(3, 5, 1)
    r1_dictionary = r1.to_dictionary()
    r2 = Rectangle.create(**r1_dictionary)
    print(r1)
    print(r1_dictionary)
#    print(', '.join([str(value) for name, value in r1_dictionary.items()]))
#    print(Rectangle.__name__)
    print(r2)
    print(r1 is r2)
    print(r1 == r2)
