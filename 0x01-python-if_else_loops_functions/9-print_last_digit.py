#!/usr/bin/python3
"""
Prints the last digit of a number
"""


def print_last_digit(number):
    last_num = abs(number % 10)
    print(f"{last_num}", end="")
    return last_num
