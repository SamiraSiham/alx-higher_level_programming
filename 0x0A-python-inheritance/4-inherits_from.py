#!/usr/bin/python3
'''Module for inherits_from method.'''


def inherits_from(obj, a_class):
    '''Determines if an object is a tru subclass of a class.'''
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False
