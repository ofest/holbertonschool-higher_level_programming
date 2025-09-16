#!/usr/bin/python3
"""Write a class Square"""


class Square:
    """Represent a Square"""
    def __init__(self, size=0, position=(0, 0)):
        """ Initialize the attribute : size"""
        self.__size = size
        self.__position = position

    """Size getter"""
    @property
    def size(self):
        return self.__size

    """Position getter"""
    @property
    def position(self):
        return self.__position

    """Size setter"""
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer.")
        if value < 0:
            raise ValueError("size must be >= 0.")
        self.__size = value

    """Position setter"""
    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers.")
        if not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers.")

    """Create public instance method: area"""
    def area(self):
        return self.__size ** 2

    """Create public instance method: my_print
    Line is not filles with spaces when position[1] > 0
    """
    def my_print(self):
        for _ in range(self.__position[1]):
            print("")
        for _ in range(self.__size):
            print(' ' * self.__position[0] + '#' * self.__size)
