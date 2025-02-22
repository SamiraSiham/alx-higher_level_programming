#!/usr/bin/python3
'''Module for square class'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''class inheriting from rectangle to
    represent a square'''
    def __init__(self, size):
        '''constructor'''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        '''return area of square'''
        return self.__size ** 2
