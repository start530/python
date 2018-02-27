#-*- coding=utf-8 -*-

import os

pa = os.path.abspath('.')+'\\'
print pa

os.path.join(pa,'testdir')
os.mkdir(pa+'testdir')
