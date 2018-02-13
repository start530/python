#!user/bin/env python2.7
#-*- coding:utf-8 -*-

'private test'
__author__ = "hzk"

class Student(object):
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

    def set_gender(gender):
        if not isinstance(gender,str):
            raise TypeError("gender type must str")
            return

        self.gender = gender

    def get_gender():
        return self.gender
