#!/usr/bin/python3
"""
Calculates a to the power
of b
"""


def pow(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    elif b < 0:
        return (1 / pow(a, -b))
    else:
        for i in range(b):
            return(a*pow(a, b-1))
