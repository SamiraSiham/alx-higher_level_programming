#!/usr/bin/python
def max_integer(my_list=[]):
    if not my_list:
        return None
    max = 0
    for i in my_list:
        if i > my_list:
            max = i
    return max
