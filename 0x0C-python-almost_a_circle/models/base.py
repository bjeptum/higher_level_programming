#!/usr/bin/python3
"""
Base module
"""


import json


class Base:
    """Base Class of the project"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """JSON string to file"""
        filename = cls.__name__ + ".json"
        json_attrs = []
        if list_objs is not None:
            for i in range(len(list_objs)):
                json_attrs.append(cls.to_dictionary(list_objs[i]))
        with open(filename, 'w') as ofile:
            return ofile.write(cls.to_json_string(json_attrs))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string"""
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = cls.__name__ = ".json"
        try:
            with open(filename, "r") as ofile:
                """string of list of dictionaries"""
                json_string = o_file.read()
                for json_string in json.loads(json_string):
                    [cls.from_json_string(json_string)]
            except:
                return []
