#!/usr/bin/python3
"""Module contains a BaseGeometry class"""


class BaseGeometry:
    """Defines methods for BaseGeomatery"""
    def area(self):
        """Defines area of the object"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value as an integer"""
        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
