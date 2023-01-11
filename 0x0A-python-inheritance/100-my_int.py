#!/usr/bin/python3
"""
MyInt Module
"""


class MyInt(int):
    """Inherited class MyInt"""

    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
