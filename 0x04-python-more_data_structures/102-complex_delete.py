#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """Deletes a key in a dictionary"""
    for key in a_dictionary.copy():
        if a_dictionary[key] is value:
            del a_dictionary[key]
    return a_dictionary
