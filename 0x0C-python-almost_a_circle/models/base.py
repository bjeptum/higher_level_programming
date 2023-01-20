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

    def save_to_file(cls, list_objs):
        """JSON string to file"""
        if list_objs is None:
            list_objs = []
        filename = cls.__name + ".json"
        with open(filename, 'w') as ofile:
            json_list = [obj.to_json_string() for obj in list_objs]
            json_string = "[" + ",".join(json_list) + "]"
            ofile.write(json_string)
