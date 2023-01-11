#!/usr/bin/python3
"""
add_attribute Module
"""


def add_attribute(obj, attr, val):
    """Adds a new attribute to the object"""
    if not hasattr(obj, '__setattr__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, val)
