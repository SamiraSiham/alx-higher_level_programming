#!/usr/bin/python3
'''Module for lookup function'''


def lookup(obj):
    '''Looks up object attributes/methods.
    Args:
        obj: object
    Returns:
        list of attributes and methods
    '''
    return dir(obj)
