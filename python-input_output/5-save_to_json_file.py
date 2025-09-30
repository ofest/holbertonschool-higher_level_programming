#!/usr/bin/python3
"""function that writes an Object to a text file, using a JSON representation"""

import json
def save_to_json_file(my_obj, filename):
    """writes an Object"""
    with open(filename, "w") as file:
        json_str = json.dumps(my_obj)
        file.write(json_str)
