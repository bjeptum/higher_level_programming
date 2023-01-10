#!/usr/bin/python3
"""
7-base_geometry module
"""


class BaseGeometry:
    """A simple class with integer validator"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates a value"""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
