#-*- coding:utf-8 -*-
'rename dir movie name'
__author__ = 'star'

import os
from langconv import *

import sys


def simplified2Trditional(content):
	'''
	简体字转成繁体字
	:param content 待转换的句子	
	'''
	sentence = Converter('zh-hant').convert(content)
	return sentence

def tranditional2Simplified(content):
	'''
	繁体字转成简体字
	:param content 待转换的句子	
	'''
	sentence = Converter('zh-hans').convert(content)
	return sentence


def searchFile2(dir):
	listdir = os.listdir(dir)
	for f in listdir:
		fpath = os.path.join(dir,f)
		if os.path.isfile(fpath):
			print fpath
			fread = open(fpath,'r')
			simCont = fread.read().decode("utf8")
			#print simCont
			fread.close()

			#simCont = simCont.encode('utf-8')
			trditionCont = simplified2Trditional(simCont)
			#print trditionCont
			fwrite = open(fpath,'w')
			fwrite.write(trditionCont)
			fwrite.close()
		elif os.path.isdir(fpath):
			searchFile2(fpath)

def searchFile(dir):
	print dir
	classPath = os.path.join(dir,'/test/')
	for root,dirs,files in os.walk(classPath):
		for file in files:
			fread = open(file,'r')
			simCont = fread.read().decode("utf8")
			print simCont
			fread.close()

			#simCont = simCont.encode('utf-8')
			trditionCont = simplified2Trditional(simCont)
			print trditionCont
			fwrite = open(file,'w')
			fwrite.write(trditionCont)
			fwrite.close()



def main():
	reload(sys)
	sys.setdefaultencoding('utf-8')
	print sys.getdefaultencoding()

	searchFile2(os.path.join(os.getcwd(),"test"))

if __name__ == '__main__':
	main()