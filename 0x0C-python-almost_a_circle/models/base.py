#!/usr/bin/python3
"""
"Almost a circle" module
"""
import json
import csv


class Base:
    """
    Define the Base class
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """initialize variables and methods"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    # JSON documentation found here:
    # https://docs.python.org/3.4/library/json.html

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        function that returns the JSON string representation of
        list_dictionaries (where each dictionary in the list represents
        an object/instance)
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        function that writes the JSON string representation of
        list_objs (e.g. [r1, r2, r3]) to a file
        function that serializes in JSON
        """
        with open("{}.json".format(cls.__name__), 'w') as f:
            if list_objs is None:
                f.write("[]")
            # write (a string representation of) a list of dictionaries
            # where each dictionary represents an object/instance
            else:
                f.write(cls.to_json_string([obj.to_dictionary()
                                            for obj in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """
        function that returns the list of the JSON string representation
        json_string (in a usable list format)
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        function that returns an instance with all attributes already set
        Note: the dictionary representation of the instance must be passed
        as a "double pointer" for changes to be permanently reflected outside
        of the create() and update() functions
        """
        if dictionary is not None and len(dictionary) > 0:
            if cls.__name__ == 'Rectangle':
                obj = cls(1, 1)
            if cls.__name__ == 'Square':
                obj = cls(1)
            obj.update(**dictionary)
            return obj

    @classmethod
    def load_from_file(cls):
        """
        function that returns a list of instances (e.g. [r1, r2, r3])
        function that deserializes in JSON
        """
        try:
            with open('{}.json'.format(cls.__name__), 'r') as f:
                f_contents = f.read()
                list_objs_dicts = cls.from_json_string(f_contents)
                list_objs = []
                for obj_dict in list_objs_dicts:
                    obj = cls.create(**obj_dict)
                    list_objs += [obj]
                return list_objs
        except:
            return []

    # CSV documentation found here:
    # https://docs.python.org/3.4/library/csv.html

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        function that writes the CSV string representation of
        list_objs (e.g. [r1, r2, r3]) to a file
        function that serializes in CSV
        """
        with open("{}.csv".format(cls.__name__), 'w+') as f:
            if list_objs is None:
                f.write("")
            # instantiate the list of dictionaries representing the
            # objects/instances present in list_objs
            list_objs_dicts = [obj.to_dictionary() for obj in list_objs]
            # DictWriter needs to be provided the fieldnames sequence as
            # 2nd (mandatory) parameter
            writer = csv.DictWriter(f, list_objs_dicts[0].keys())
            # write the fieldnames sequence(row #1) in file
            writer.writeheader()
            # write the value sequences
            # as strings in the CSV files
            # row by row, for each object
            writer.writerows(list_objs_dicts)

    @classmethod
    def load_from_file_csv(cls):
        """
        function that returns a list of instances (e.g. [r1, r2, r3])
        function that deserializes in CSV
        """
        try:
            with open('{}.csv'.format(cls.__name__), 'r') as f:
                reader = csv.DictReader(f)
                # reader is a dict of dict of key and value strings
                list_objs = []
                # initialize a new list that will store
                # the instances by name (e.g. r1, r2)
                for row in reader:
                    # each row is a dict of key and value strings
                    # representing an object/instance
                    obj_dict = {}
                    # initialize a new dict that will store
                    # the keys as strings and the values as ints
                    # (here the values must be converted from
                    # string to ints)
                    for name, value in row.items():
                        # iterate through each
                        # row dict
                        obj_dict[name] = int(value)
                        # store the value-pairs in
                        # the new dict
                    obj = cls.create(**obj_dict)
                    # create the object/instance
                    # from its dictionary
                    # representation
                    list_objs += [obj]
                    # append the new object/instance
                    # to the list of object/instances
                return list_objs
                # returns the (simple) list of instances
        except:
            return '[]'
