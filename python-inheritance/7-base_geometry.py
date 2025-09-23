#!/usr/bin/python3
""" Module contains a baseGeometry class"""


class BaseGeometry():
    """Public instance method"""
    def area(self):
        raise Exception("area() is not implemented")

    """Public instance method that validates the value"""
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise TypeError("<name> must be greater than 0")
