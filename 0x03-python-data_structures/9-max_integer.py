#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    max_val = my_list[0]
    i = 1
    while i < len(my_list):
        if my_list[i] > max_val:
            max_val = my_list[i]
        i += 1
    return max_val
