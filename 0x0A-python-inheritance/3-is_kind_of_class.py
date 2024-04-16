#!/usr/bin/python3
'''Modul for is_kind_of_class method.'''


def is_kind_of_class(obj, a_class):
    '''Determines if the object is an instance of 
    a subclass of a_class.'''
    if isinstance(obj, a_class):
        return True
    return False
