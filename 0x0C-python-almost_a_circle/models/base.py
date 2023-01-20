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
        filename = type(list_objs[0]).__name__ + ".json"
        with open(filename, 'w') as ofile:
            if list_objs is None:
                return ofile.write(cls.to_json_string(None))
            json_attrs = []
            for objs in list_objs:
                json_attrs.append(objs.to_dictionary())
                return ofile.write(cls.to_json_string(json_attrs))
