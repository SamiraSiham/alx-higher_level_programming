#!/usr/bin/python3
def print_sorted_dictionnary(a_dictionnary):
    for k in sorted(a_dictionnary.keys()):
        print("{}: {}".format(k, a_dictionnary[k]))
