#!/usr/bin/python3
"""
Class module
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle subclass"""
    def __init__(self, width, height):
        """initialization method"""
        self.__width = width
        self.__height = height
        super(Rectangle, self).integer_validator('width', self.__width)
        super(Rectangle, self).integer_validator('height', self.__height)
