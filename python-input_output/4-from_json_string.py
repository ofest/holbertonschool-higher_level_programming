#!/usr/bin/python3
"""function that returns an object (Python data structure) 
represented by a JSON string"""

import json
def from_json_string(my_str):
    """returns an object of a JSON string"""
    my_str = json.loads(my_str)
    return my_str
