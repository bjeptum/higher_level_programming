#!/usr/bin/python3
"""
Class to JSON Module
"""


def class_to_json(obj):
    """Returns dictionary description for JSON serialization of object"""
    return obj.__dict__
