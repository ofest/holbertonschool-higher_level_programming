#!/usr/bin/python3
"""Module contains the function is_same_class"""


def is_same_class(obj, a_class):
    """Returns True if the object is exactly an instance of the
    specified class;
    otherwise, False"""
    if obj.__class__ == a_class:
        return True
    else:
        return False
