#!/usr/bin/python3
"""
module 1
"""


def load_from_json_file(filename):
    """function1"""
    import json
    with open(filename, 'r') as file:
        return json.load(file)
