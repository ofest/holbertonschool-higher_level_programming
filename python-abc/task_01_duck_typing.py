#!/usr/bin/env python3


from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes"""

    @abstractmethod
    def area(self):
        """Return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Return the perimeter of the shape."""
        pass


class Circle(Shape):
    """Circle shape defined by its radius."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Method that return the area of a circle"""
        return math.fabs(math.pi * (self.radius**2))


    def perimeter(self):
        """Method that return the perimeter of a circle """
        return math.fabs(2 * math.pi * self.radius)

class Rectangle(Shape):
    """Rectangle shape defined by width and height."""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(obj):
    """Function that print shape information"""
    print("Area: {}".format(obj.area()))
    print("Perimeter: {}".format(obj.perimeter()))
