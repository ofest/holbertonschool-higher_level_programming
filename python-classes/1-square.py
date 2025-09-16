#!/usr/bin/python3
"""Write a class Square that defines square calling 0 square.py"""


class Square:
    """Size and self class"""
    def __init__(self, size):
        self.__size = size
    """Size class"""
    def get_size(self):
        return self.__size
