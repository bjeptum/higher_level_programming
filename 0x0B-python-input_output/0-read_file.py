#!/usr/bin/python3
"""
0-read_file module
"""


def read_file(filename=""):
    """reads a text file (UTF8)"""
    with open(filename, "r") as f:
        print(f.read())
