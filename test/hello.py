#!user/bin/env python2.7
#-*- coding = utf-8 -*-

'a module test'
__author__ = "star"

import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print("hello world")
    elif len(args) == 2:
        print("hello,%s" % args[1])
    else:
        print("too many arguments")

if __name__ == "__main__":
    test();




