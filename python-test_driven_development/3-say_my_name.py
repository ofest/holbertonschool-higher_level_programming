#!/usr/bin/python3
"""Module contains a function that prints
    My name is {first_name}{last_name}
    TypeError exception with the message first_name must be a string or last_name must be a string
"""
def say_my_name(first_name, last_name=""):
    """
    Function that prints, first_name and last name
    """
    if isinstance(first_name, str) is False:
        raise TypeError("first_name must be a string")
    if isinstance(last_name, str) is False:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
