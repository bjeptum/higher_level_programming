#!/usr/bin/python3
"""
1-write_file Module
"""


def write_file(filename="", text=""):
    """Writes a string to a text file"""
    with open(filename, 'w') as f:
        f.write(text)
        return len(text)
