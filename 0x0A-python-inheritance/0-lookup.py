#!/usr/bin/python3
def lookup(obj):
    """Lists available attributes and methods of an object"""
    attributes = dir(obj)
    print(attributes)
