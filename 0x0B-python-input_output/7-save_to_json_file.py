#!/usr/bin/python3
"""
module 1
"""


def save_to_json_file(my_obj, filename):
    """function1"""
    import json
    with open(filename, 'w') as file:
        file.write(json.dumps(my_obj))
