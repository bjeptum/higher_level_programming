#!/usr/bin/python3
"""
1-my_list module
An inherited xlass that prints a sorted list
"""


class MyList(list):
    """Inherited Class"""
    def print_sorted(self):
        """Prints a sorted list"""
        print(sorted(self))
