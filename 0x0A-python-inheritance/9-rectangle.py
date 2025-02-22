#!/usr/bin/python3
'''Module for rectangle class.'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''A subclass that represents a rectangle'''
    def __init__(self, width, height):
        '''constructor'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        '''calculate area of rectangle'''
        return self.__width * self.__height

    def __str__(self):
        '''return string representation of instance'''
        return f'[Rectangle] {self.__width}/{self.__height}'
