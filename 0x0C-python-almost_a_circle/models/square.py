#!/usr/bin/python3
"""
Square module
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Class instantiation"""
        super().__init__(size, size, x, y, id)

    def area(self):
        """Returns area of the square"""
        a = pow(self.width, 2)
        return a

    def __str__(self):
        """Returns string representation of the object"""
        return (f'[Square] ({self.id}) {self.x} / {self.y} - {self.width}')