#-*- coding: utf-8 -*-

'search file'
__author__ = 'star'

import os

def search_file(filePath,filename):
	#获取当前目录下所有的文件
    list = os.listdir(filePath)
    for f in list:
    	#通过合并的方法获得当前查询的f文件路径
    	fpath = os.path.join(filePath,f)
    	#判断f是文件还是文件夹，如果是文件，通过split[1]获得文件扩展名，判断扩展名是否为我们要查询的
    	#如果是文件夹，那么以这个文件夹为节点，递归的一层层查询
    	if os.path.isfile(fpath) and filename in os.path.split(fpath)[1]:
    		print "found file,path =",fpath
    	elif os.path.isdir(fpath):
    		search_file(fpath,filename)

inputfile = raw_input("please input search file name:")

search_file(os.path.abspath('.'),inputfile)