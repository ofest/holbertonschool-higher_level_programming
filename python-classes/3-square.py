#!/usr/bin/python3
"""Write a class Square"""


class Square:
    """Represent a Square"""
    def __init__(self, size=0):
        """Initialize the private instance attribute: size
        Raise the TypeError or ValueError according to given condition"""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer.")
        if size < 0:
            raise ValueError("size must be >= 0.")

    def get_size(self):
        return self.__size

    """Create public instance method: def area(self)"""
    def area(self):
        return self.__size ** 2
