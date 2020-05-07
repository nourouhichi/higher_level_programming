#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) is 0:
        return 0
    up = sum(map(lambda i: i[0] * i[1], my_list))
    down = sum(map(lambda i: i[1], my_list))
    return up / down
