#!/usr/bin/python3
'''module for append_write function'''


def append_write(filename="", text=""):
    '''append text to file with utf-8.'''
    with open(filename, "a", encoding='utf-8') as f:
        f.write(text)
