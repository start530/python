#!user/bin/env python2.7
#-*- coding = utf-8 -*-

'class test'
__author__ = "star"

class star(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def print_log(self):
        print("name = %s,age = %s" % (self.name,self.age))


a = star("star",15)
print(a.name,a.age)
a.print_log()
