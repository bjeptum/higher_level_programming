#!/usr/bin/python3
import magic_calculation_102
from magic_calculation_102 import add, sub


def magic_calculation(a, b):
    c = 0
    if a > b:
        c = sub(a, b)
        if c == 4:
            c = add(c, 10)
    if a < b:
        c = add(a, b)
        for i in range(4, 7):
            c = add(a, i)
    else:
        c = sub(a, b)
    return c
