#!/usr/bin/python3
'''load_from_json_file function'''


import json


def load_from_json_file(filename):
    '''create object from json file'''
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
