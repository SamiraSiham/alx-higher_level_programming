#!/usr/bin/python3
'''student class module'''


class Student:
    '''representing a student'''
    def __init__(sef, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''return dict representation of student instance'''
        return self.__dict__
