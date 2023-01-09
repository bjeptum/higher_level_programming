#!/usr/bin/python3
"""
1-my_list module
An inherited class
"""


class MyList(list):
    """MyList Class"""
    def print_sorted(self):
        """Prints a sorted list"""
        print(sorted(self))
