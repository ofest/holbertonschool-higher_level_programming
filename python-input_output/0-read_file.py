#!/usr/bin/python3
""" function that reads a text file"""


def read_file(filename=""):
    """reads a text file"""
    with open(filename) as file_object:
        contents = file_object.read()
        print(contents, end="")
