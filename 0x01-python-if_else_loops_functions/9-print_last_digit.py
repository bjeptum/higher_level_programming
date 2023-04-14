#!/usr/bin/python3
"""
Prints the last digit of a number
"""


def print_last_digit(number):
    if number < 0:
        last_num = number % (-10)
    else:
        last_num = number % 10

    print(f"{last_num}")
