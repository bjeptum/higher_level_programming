#!/usr/bin/python3
"""
5-save_to_json_file Module
"""


import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation"""
    with open(filename, 'w') as ofile:
        json.dump(my_obj, ofile)
