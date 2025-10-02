#!/usr/bin/env python3

import csv
import json


def convert_csv_to_json(filename):
    with open(filename, "r") as f:
        csv_list = list(csv.DictReader(f))

    with open("data.json", "w") as jsonf:
        jsonf.write("[\n")
        separator = ("")
        for i in csv_list:
            jsonf.write(separator + "    " + json.dumps(i))
            separator = (",\n")
        jsonf.write("\n]\n")
