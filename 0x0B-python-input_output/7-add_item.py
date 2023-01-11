#!/usr/bin/python3
"""
Add item module
"""


import sys
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation"""
    with open(filename, 'w') as ofile:
        json.dump(my_obj, ofile)


def load_from_json_file(filename):
    """Creates an Object from a JSON file"""
    with open(filename, 'r') as ofile:
        json_data = ofile.read()
        return json.loads(json_data)


# Get command line arguments
args = sys.argv[1:]


# Load existing data from file
try:
    data = load_from_json_file("add_item.json")
except (FileNotFoundError, json.decoder.JSONDecodeError):
    data = []

# Add command line arguments to data
data.extend(args)

# Save data to file
save_to_json_file(data, 'add_item.json')
