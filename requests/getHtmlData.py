#!/user/bin/env python2.7
# -*- coding:utf-8 -*-
from typing import Any, Union

__author__ = 'star'
'''get html data,save file
'''

import requests
import os
import sys


reload(sys)
sys.setdefaultencoding('utf-8')

URL = 'http://www.baidu.com'


def savefile(data):
	"""
	:将获取的数据写入文件
	:param data: 传入的数据
	:return: null
	"""

	filePath = os.path.join(os.getcwd(), 'htmlData.md')
	with open(filePath, 'wb') as f:
		f.write(data)


def gethtmldata():
	"""
	抓取网页数据
	"""
	header = {'User-Agent':  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
	response = requests.get(URL, headers=header)
	# response.encoding = 'utf-8'

	data = response.text
	print data

	savefile(data)


if __name__ == '__main__':
	gethtmldata()

