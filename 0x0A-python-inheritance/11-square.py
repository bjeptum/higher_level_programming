#!/usr/bin/python3
"""
11-square module
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A subclass of Rectangle"""
    def __init__(self, size):
        """Instantiation method"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calculates area"""
        return self.__size ** 2

    def __str__(self):
        """Returns a square description"""
        return "[Square]" + str(self.__size) + "/" + str(self.__size)
