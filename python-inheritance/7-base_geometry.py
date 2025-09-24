#!/usr/bin/python3
"""Module contains a BaseGeometry class"""


class BaseGeometry:
    """Defines methods for BaseGeometry"""
    def area(self):
        """Defines area of the object"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is a positive integer"""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
