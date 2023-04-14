#!/usr/bin/python3
"""
Prints the last digit of a number
"""


def print_last_digit(number):
    if number < 0:
        last_num = number % (-10)
    else:
        last_num = number % 10
    last_num = abs(last_num)
    print(f"{last_num}", end="")
    return last_num
