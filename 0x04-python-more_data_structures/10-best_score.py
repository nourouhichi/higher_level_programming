#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max_v = 0
    for key, value in a_dictionary.items():
        if max_v < value:
            max_k, max_v = key, value
    return max_k
