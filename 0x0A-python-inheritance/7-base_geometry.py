#!/usr/bin/python3
'''Module for BaseGeometry class.'''


class BaseGeometry:
    '''BaseGeometry class'''
    def area(self):
        '''Method to compute area'''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''Check if value is an integer and is positive'''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
