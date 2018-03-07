#!/user/bin/python
#-*- coding:utf-8 -*-

'hash test'
__author__ = 'star'

import hashlib

md5 = hashlib.md5()
md5.update('star is'.encode('utf-8'))
md5.update('so cool'.encode('utf-8'))
print md5.hexdigest()
