#!/usr/bin/python3
"""
Function that represents the Pascals triangle
"""


def pascal_triangle(n):
    
    triangle = []

    if n <= 0:
        return []

    triangle.append([1])

    for i in range(1, n):
        row = [1]
        last_row = triangle[i - 1]

        for j in range(1, i):
            row.append(last_row[j - 1] + last_row[j])

        row.append(1)
        triangle.append(row)
    return triangle