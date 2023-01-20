#!/usr/bin/python3
"""
Base module
"""
import json
import csv


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
        filename = ((cls.__name__) + ".json")
        elem = []
        with open(filename, 'r') as rfile:
            text = rfile.read()
        text = cls.from_json_string(text)
        for item in text:
            if type(item) == dict:
                elem.append(cls.create(**item))
            else:
                elem.append(item)
        return elem

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves to a CSV File"""
        elem = [item.to_dictionary() for item in list_objs]
        filename = (cls.__name__) + ".csv"
        with open(filename, 'w') as save_file:
            write_to = csv.DictWriter(save_file, elem[0].keys())
            write_to.writeheader()
            write_to.writerows(elem)

    @classmethod
    def load_from_file_csv(cls):
        """Loads from a CSV file"""
        elem = []
        elem_dict = []
        filename = (cls.__name__) + ".csv"
        with open(filename, 'r') as read_file:
            read_from = csv.DictReader(read_file)
            for item in read_from:
                for key, value in dict(item).items:
                    elem_dict(key)
                elem.append(create(**elem_dict))
        return elem
