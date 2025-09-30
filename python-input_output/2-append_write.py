#!/usr/bin/python3
""" function that writes a string to a text file """


def append_write(filename="", text=""):
    with open(filename, 'a') as file_object:
        return file_object.write(text)
