#!/usr/bin/python3
"""
10-square module
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A subclass of Rectangle"""
    def __init__(self, size):
        """Instantiation method"""
        super().__init__(size, size)
        self.__size = size

        def area(self):
            """Calculates area"""
            return self.__size ** 2
