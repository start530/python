#!/user/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'start530'

import os
import requests
import re
from bs4 import BeautifulSoup
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

URL = 'https://youhuiyu.kuaizhan.com/96/14/p5559064779e0dd'
# URL = 'https://youhuiyu.kuaizhan.com/99/78/p555251718cad66'

# 在这里修改游戏名
game_name = '活动预告'

file_path = os.path.join(os.getcwd(),game_name+'.txt')


def savefile(data):
	# 存储数据
	fd = open(unicode(file_path,'utf-8'),'w')
	fd.write(data)
	fd.close()


def get_advance_data():
	# 读取数据
	# 返回列表
	headers = {'User-Agent':  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
	response = requests.get(URL, headers=headers)
	tap_html = response.content
	
	# 解析数据data_list
	data_list = {}
	ad_soup = BeautifulSoup(tap_html,'lxml')
	# 获取基础信息
	content_div = ad_soup.find_all('div',class_='mod mod-html')
	print content_div
	for i in content_div:
		print i.text 
	

	

if __name__ == '__main__':
	get_advance_data()



