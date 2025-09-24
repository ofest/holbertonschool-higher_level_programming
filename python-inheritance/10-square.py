#!/usr/bin/python3
"""A subclass Square derived from Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square using attributes from  BaseGeometry and
    the subclass Rectangle."""
    def __init__(self, size):

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
        self.__size = size
