#!/usr/bin/python3
"""function that returns the JSON representation of an object"""

import json
def to_json_string(my_obj):
    """JSON representation of an object"""
    my_obj = json.dumps(my_obj)
