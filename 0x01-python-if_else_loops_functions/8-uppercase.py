#!/usr/bin/python3
"""
Prints a string in uppercase
Not allowed to import any module
No use of str.upper() and str.isupper()
"""


def uppercase(str):
    uppercase_str = ""
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            new_c = chr(ord(char) - 32)
            uppercase_str += new_c
        else:
            uppercase_str += char
    print("{}\n".format(uppercase_str), end='')
