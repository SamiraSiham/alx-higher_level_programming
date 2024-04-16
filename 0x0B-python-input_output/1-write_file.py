#!/usr/bin/python3
'''module for write_file function'''


def write_file(filename="", text=""):
    '''write a string to a text file (utf-8)
    Args:
        filename: file to write in
        text: string to be written in file
    Returns:
        number of characters written
    '''
    with open(filename, "w", encoding='utf-8') as f:
        return f.write(text)
