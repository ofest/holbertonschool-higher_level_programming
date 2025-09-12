#!/usr/bin/python3
"""Module that contains a function to add two integers.
"""


def add_integer(a, b=98):
    """Return the sum of a and b.

    Args:
        a: int or float.
        b: int or float, default is 98.

    Raises:
        TypeError: If a or b are not int or float.

    Returns:
        int: The sum of a and b after casting floats to int.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
