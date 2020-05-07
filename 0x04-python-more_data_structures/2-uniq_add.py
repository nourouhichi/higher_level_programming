#!/usr/bin/python3
def uniq_add(my_list=[]):
    adds = 0
    for i in set(my_list):
            adds = adds + i
    return adds
