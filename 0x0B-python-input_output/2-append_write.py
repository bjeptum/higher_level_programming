#!/usr/bin/python3
"""
2-append_write module
"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file"""
    with open(filename, "a") as f:
        f.write(text)
        return len(text)
