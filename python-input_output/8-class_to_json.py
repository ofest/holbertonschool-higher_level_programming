#!/usr/bin/python3


def class_to_json(obj):

    serialized_dict = {}

    for key, value in vars(obj).items():

        if isinstance(value, (list, dict, str, int, bool)):
            serialized_dict[key] = value

    return serialized_dict
