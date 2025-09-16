#!/usr/bin/python3
"""Write a class Square"""


class Square:
    def __init__(self, size=0):
        """Represent a Square"""
        self.__size = size
        """Initialize the private instance attribute to define a square
        Raise the type or value error exception according to given condition"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer.")
        elif size < 0:
            raise ValueError("size must be >= 0.")

    def get_size(self):
        return self.__size
