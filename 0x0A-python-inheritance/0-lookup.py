#!/usr/bin/python3
def lookup(obj):
    """Lists available attributes and methods of an object"""
    attributes_and_methods = dir(obj)
    print(attributes_and_methods)
