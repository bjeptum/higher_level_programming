#!/usr/bin/python3
"""
Rectangle module
"""


from models.base import Base


class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Class instantiation"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Returns Width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        self.integer_validator("width", value, False)
        self.__width = value

    @property
    def height(self):
        """Returns height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        self.integer_validator("height", value, False)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.integer_validator("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.integer_validator("y", value)
        self.__y = value

    def integer_validator(self, name, value, z=True):
        """Validates a value"""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if z and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not z and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        """Calculates area"""
        return self.__width * self.__height

    def display(self):
        """Prints in stdout the Rectangle instance with the character #"""
        d = ('\n'.join('#' * self.__width for _ in range(self.__height)))
        print(d)

    def __str__(self):
        """Returns string representation of the object"""
        return (f'[Rectangle] ({self.id}) \
{self.__x}/{self.__y} - {self.__width}/{self.__height}')
