#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for i in a_dictionary.keys():
        if key is i:
            a_dictionary[i] = value
            return a_dictionary
        else:
            a_dictionary[key] = value
            return a_dictionary
