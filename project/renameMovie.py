#-*- coding:utf-8 -*-
'rename dir movie name'
__author__ = 'star'

import os

#重命名文件，给目录下的文件按顺序编号
def changeNameByNum(path):
	listdir = os.listdir(path)
	num = 0
	for f in listdir:
		fpath = os.path.join(path,f)
		if os.path.isfile(fpath):
			#获取文件的扩展名
			file_type = os.path.splitext(fpath)[1]
			new_name = str(num)
			num = num+1
			os.rename(fpath,path+new_name+file_type)

#test
changeNameByNum(os.getcwd()+'/movie/')

#重命名文件，在文件前加上其他文字
'''
def changeName(path):
	listdir = os.listdir(path)
	print listdir
	for f in listdir:
		fpath = os.path.join(path,f)
		#判断是文件还是文件夹，如果是文件夹，要递归处理
		if os.path.isfile(fpath):
			new_name = 'star_' + f
			old_name = f
			os.rename(path+old_name,path+new_name)
			print path + '|' + old_name + ' => ' + new_name
		elif os.path.isdir(fpath):
			changeName(fpath+'/')

changeName(os.getcwd() + '/movie/')
'''

print "批量重命名完成"

