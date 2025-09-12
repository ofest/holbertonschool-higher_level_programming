#!/usr/bin/python3
"""Module contains a function that adds 2 integers"""


def add_integer(a, b=98):
    """Function that adds 2 integers
    integers (a)
    integers (b)
    return (a + b)
    """
    if isinstance(a, (int, float)) is False:
        raise TypeError("a must be an integer")
    if isinstance(b, (int, float)) is False:
        raise TypeError("b must be an integer")
    a = int(a) 
    b = int(b)
    return a + b
