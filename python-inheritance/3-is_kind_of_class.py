#!/usr/bin/python3
""" Module contains a function that checks the kind of class"""


def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance or;
    inherited instance of the specified class;
    Return False, otherwise"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
