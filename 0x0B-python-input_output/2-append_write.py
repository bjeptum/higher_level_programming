#!/usr/bin/python3
"""
2-append_write module
"""


def append_write(filename="", text=""):
    with open(filename, "a") as f:
        f.write(text)
        return len(text)
