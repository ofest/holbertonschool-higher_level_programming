#!/usr/bin/python3
"""
Function that represents the Pascals triangle
"""


def pascal_triangle(n):
    """Function that creates a pascal_triangle"""
    if n <= 0:
        return []

    res = []
    for i in range(n):
        to_add = [1]

        for j in range(1, i):
            to_add.append(res[i - 1][j - 1] + res[i - 1][j])

        if i > 0:
            to_add.append(1)

        res.append(to_add)

    return res
