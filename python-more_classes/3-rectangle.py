#!/usr/bin/python3
"""Write a class Rectangle"""


class Rectangle:
    """Represents a rectangle"""

    def __init__(self, width=0, height=0):
        """Defines a rectangle by width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Heigth setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return (0)
        else:
            return (2 * (self.width + self.height))
    print

    def __str__(self):
        """Returns the printable representation of the rectangle"""
        if self.width == 0 or self.height == 0:
            return ("")
        rectangle_str = ""
        for _ in range(self.height):
            rectangle_str += '#' * self.width + "\n"
        return rectangle_str.rstrip()
