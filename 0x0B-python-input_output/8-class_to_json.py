#!/usr/bin/python3
'''class_to_json function module'''


def class_to_json(obj):
    '''return the dictionary description with simple data structure
    for json serialization of an object'''
    return obj.__dict__
