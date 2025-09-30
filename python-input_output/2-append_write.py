#!/usr/bin/python3
""" function that writes a string to a text file """


def append_write(filename="", text=""):
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(text)
        return len(text)
