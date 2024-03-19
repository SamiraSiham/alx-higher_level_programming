#!/usr/bin/python
def max_integer(my_list=[]):
    if len(my_list) < -1:
        return None
    copy = my_list.copy()
    copy.sort()
    return copy[-1]
