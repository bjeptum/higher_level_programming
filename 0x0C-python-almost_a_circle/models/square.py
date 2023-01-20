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

    @property
    def size(self):
        """Returns size of one side of square"""
        return super().width(size)

    @size.setter
    def size(self, value):
        """Returns size of one side of square"""
        self.width = value
        self.height = value

    def area(self):
        """Returns area of the square"""
        a = pow(self.width, 2)
        return a

    def __str__(self):
        """Returns string representation of the object"""
        return ('[{}] ({}) {}/{} - {}'.format(self.__class__.__name__,
                self.id, self.x, self.y, self.width))
