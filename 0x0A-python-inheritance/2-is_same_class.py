#!/usr/bin/python3
'''is_same_class method'''


def is_same_class(obj, a_class):
    '''check if an object is an instance of the specified class
        Args:
            obj: object to check
            a_class: class to compare object to
        Returns:
            True if object is instance of the class, False otherwise
    '''
    return type(obj) == a_class
