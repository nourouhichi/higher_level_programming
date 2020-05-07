#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for _key in a_dictionary.keys():
        if _key is key:
            del a_dictionary[_key]
            return a_dictionary
    else:
        return a_dictionary
