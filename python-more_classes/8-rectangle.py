#!/usr/bin/python3
"""Write a class Rectangle"""


class Rectangle:
    """Represents a rectangle"""

    """Initialize counter at the class level"""
    number_of_instances = 0

    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Defines a rectangle by width and height"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
        """Increment when a new instance is created"""

    @property
    def width(self):
        """Width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Heigth setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return (0)
        else:
            return (2 * (self.width + self.height))
    print

    def __str__(self):
        """Returns the printable representation of the rectangle"""
        if self.width == 0 or self.height == 0:
            return ("")
        rectangle_str = ""
        for _ in range(self.height):
            rectangle_str = (str(self.print_symbol) * self.width + "\n") \
                * self.height + "\n"
        return rectangle_str.rstrip()

    def __repr__(self):
        """Returns the string representation of rectangle"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
        """Decrement the count when deleted"""

    @classmethod
    def Instances(cls):
        """Returns the number of current Rectangle instances"""
        return cls.number_of_instances

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance (rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance (rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        
        area_1 = rect_1.area()
        area_2 = rect_2.area()

        if area_1 >= area_2:
            return rect_1
        else:
            return rect_2
