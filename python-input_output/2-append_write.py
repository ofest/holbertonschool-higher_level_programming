#!/usr/bin/python3
""" function that writes a string to a text file """


def append_write(filename="", text=""):
    """Appends a string at the end of a text file"""
    with open(filename, 'a') as file_object:
        return file_object.write(text)
