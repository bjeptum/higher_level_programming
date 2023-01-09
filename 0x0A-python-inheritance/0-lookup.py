#!/usr/bin/python3
"""
0-lookup module
Search available attributes and methods of an object
"""


def lookup(obj):
    """Lists available attributes and methods of an object"""
    attributes_and_methods = dir(obj)
    print(attributes_and_methods)
