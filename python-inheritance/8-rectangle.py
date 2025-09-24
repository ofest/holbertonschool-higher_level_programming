#!/usr/bin/python3
""" Module contains a baseGeometry class"""


class BaseGeometry():
    """Public instance method"""
    def area(self):
        raise Exception("area() is not implemented")

    """Public instance method that validates the value"""
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Represents a rectangle using attributes from  BaseGeometry."""

    def __init__(self, width, height):
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
