#!/usr/bin/python3
"""Write a class Student that defines a student by:
"""


class Student ():

    def __init__(self, first_name, last_name, age):
        """Public instance attributes"""
        self.first_name = first_name

        self.last_name = last_name

        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of a Student"""
        self.__dict__
        result = {}
        if attrs is None:
            return self.__dict__
        if isinstance(attrs, list):
            for attr in attrs:
                if hasattr(self, attr):
                    result[attr] = getattr(self, attr)
        return result
    
    def reload_from_json(self, json):
        """ replaces all attributes of the Student instance"""
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
