#-*- coding: utf-8 -*-

'os rename'
__author__ = 'star'

import os

fileName = raw_input("please input file name...")

print("old file name:%s"% fileName)

#check file is in dir
def checkFile(filename):
	list = os.listdir('.')
	print list

	for f in list:
		if f == filename:
			print("file in dir")
			return 
	return 0


#if checkFile(fileName):
p_tuple = os.path.splitext(fileName)

print p_tuple[1]

if p_tuple[1] != '.txt':
	print("file must txt")
else:
	print("file correct")
	try:
		print "try"
		os.rename(fileName,p_tuple[0]+'.py')
	except Exception,e:
		print "exception"
		print Exception,':',e
	finally:
		print "finally"
	print "hahahhaha"

print "haha"
