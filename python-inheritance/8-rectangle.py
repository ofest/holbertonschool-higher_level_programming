#!/usr/bin/python3
""" Module defines a Rectangle class that inherits from BaseGeometry """


BaseGeometry = __import__('7-base_geometry').BaseGeometry

""" Module defines a Rectangle class that inherits from BaseGeometry """


class Rectangle(BaseGeometry):
    """Represents a rectangle, inherits from BaseGeometry."""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
