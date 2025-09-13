#!/usr/bin/python3
"""This module contains function that indents text"""


def text_indentation(text):
    """Function that prints a text with 2 new lines
    after ., ?, :"""
    if type(text) != str:
        raise TypeError("text must be a string")

    c = 0
    newstring = ""
    for i in text:
        if c == 1:
            newstring = ""
            c = 0
        if i not in "?:.":
            newstring += i
        else:
            newstring += i
            print(newstring.strip())
            print()
            c = 1
    if c == 0 and '\n' not in newstring:
        print(newstring.strip(), end="")
    elif c == 0:
        print(newstring.strip())
