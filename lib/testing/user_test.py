#!/usr/bin/env python3

from user import User
# user.py
class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class TestUser:
    '''Class "User" in user.py'''

    def test_is_class(self):
        '''is a class.'''
        assert(object in User.__bases__)

    def test_initializes_with_names(self):
        '''initializes with first and last name.'''
        my_user =User("My", "User")
        assert((my_user.first_name, my_user.last_name) == ("My", "User"))