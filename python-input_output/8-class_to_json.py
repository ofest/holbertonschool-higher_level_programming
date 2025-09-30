#!/usr/bin/python3
"""function that returns the dictionary
description with simple data structure """


def class_to_json(obj):
    """returns the dictionary"""
    serialized_dict = {}

    for key, value in vars(obj).items():

        if isinstance(value, (list, dict, str, int, bool)):
            serialized_dict[key] = value

    return serialized_dict
