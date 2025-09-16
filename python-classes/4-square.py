#!/usr/bin/python3
"""Write a class Square"""


class Square:
    """Represent a Square"""
    def __init__(self, size=0):
        self.__size = size

    """Getter"""
    @property
    def size(self):
        return self.__size
    """Setter"""
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer.")
        if value < 0:
            raise ValueError("size must be >= 0.")
        self.__size = value

    """Create public instance method: def area(self)"""
    def area(self):
        return self.__size ** 2
