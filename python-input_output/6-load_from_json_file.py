#!/usr/bin/python3


import json
def load_from_json_file(filename):
    with open(filename, "r") as file:
        json_str = file.read ()
        return json.loads(json_str)
