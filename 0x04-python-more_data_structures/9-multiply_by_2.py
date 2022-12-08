#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    for key in a_dictionary:
        a_dictionary[key] *= 2


def print_sorted_dictionary(a_dictionary):
    for key in sorted(a_dictionary.keys()):
        print("{}: {}".format(key, a_dictionary[key]))
