#!/usr/bin/python3
"""
Finds all multiples of 2 in a list
"""


def divisible_by_2(my_list=[]):
    result = []
    for num in my_list:
        if num % 2 == 0:
            result.append(True)
        else:
            result.append(False)
    return result
