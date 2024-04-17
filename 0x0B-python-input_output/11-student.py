#!/usr/bin/python3
'''student class module'''


class Student:
    '''representing a student'''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''return dict representation of student instance
        if attrs is a list of string, only names will be retrieved
        otherwise, all attrs will be retrieved
        '''
        try:
            for attr in attrs:
                if type(attr) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        my_dict = dict()
        for key, value in self.__dict__.items():
            if key in attrs:
                my_dict[key] = value
        return my_dict

    def reload_from_json(self, json):
        '''replace all atts of the student instance
        with ones from the json arg'''
        for key, value in json.items():
            if key in self.__dict__:
                self.__dict__[key] = value
