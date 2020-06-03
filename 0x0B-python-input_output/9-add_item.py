#!/usr/bin/python3
"""
module 1
"""


from sys import argv
saving = __import__("7-save_to_json_file").save_to_json_file
loading = __import__("8-load_from_json_file").load_from_json_file
try:
    x = loading("add_item.json")
except Exception:
    x = []
for arg in argv[1:]:
    x.append(arg)
saving(x, "add_item.json")
