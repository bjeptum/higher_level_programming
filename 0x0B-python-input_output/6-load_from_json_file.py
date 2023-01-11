#!/usr/bin/python3
"""
Load_from_json_file Module
"""


import json


def load_from_json_file(filename):
    """Creates an Object from a JSON file"""
    with open(filename, 'r') as json_f:
        json_data = json_f.read()
        return json.loads(json_data)

