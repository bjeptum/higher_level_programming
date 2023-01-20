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
        return super().width

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

    def update(self, *args, **kwargs):
        """Updates instance attributes via non-keyword & keyword args"""
        original = [self.id, self.size, self.x, self.y]
        if args:
            new_args = list(args[:len(args)]) + original[len(args):]
        if not args:
            parsed_kwargs = [
                    kwargs.get('id'),
                    kwargs.get('size'),
                    kwargs.get('x'),
                    kwargs.get('y')
                    ]
            new_args = [
                    parsed_kwargs[i] if parsed_kwargs[i] is not None
                    else original[i]
                    for i in range(len(original))
                    ]
        if args or kwargs:
                (self.id, self.size, self.x, self.y) = new_args
