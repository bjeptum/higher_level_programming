#!/usr/bin/python3
"""
Checks for lowercase character
"""


def islower(c):
    new_c = ord(c)
    if new_c >= 97 and new_c <= 122:
        return True
    else:
        return False
