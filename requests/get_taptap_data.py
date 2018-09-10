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

# 这这里修改游戏网址
TAP_URL = 'https://www.taptap.com/app/67156'

# 在这里修改游戏名
game_name = '富甲封神传'

file_path = os.path.join(os.getcwd(),game_name+'.txt')


def analyze_data(data):
	# 解析读取的数据

	fd = open(file_path,'w')
	game_name = data['game_name'] + '\n'
	fd.write(game_name)

	game_company = data['game_company'] + '\n'
	fd.write(game_company)

	count_stats = data['stats_list']
	for stats in count_stats:
		fd.write(stats + '\t')

	fd.write(stats + '\t')

	fd.close()

def savefile(data):
	# 存储数据
	fd = open(unicode(file_path,'utf-8'),'w')
	fd.write(data)
	fd.close()


def get_taptap_data():
	# 读取数据
	# 返回列表
	headers = {'User-Agent':  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
	response = requests.get(TAP_URL, headers=headers)
	tap_html = response.text
	
	# 解析数据data_list
	data_list = {}
	tap_soup = BeautifulSoup(tap_html,'lxml')
	# 获取基础信息
	main_header_text = tap_soup.find('div',class_='main-header-text')
	# print main_header_text
	# 游戏名和公司名
	game_name = main_header_text.find('h1').get_text()
	game_company = main_header_text.find('span',attrs={'itemprop':'name'}).get_text()
	# 安装，预约，关注
	count_stats = main_header_text.find_all('span',class_='count-stats')
	print type(count_stats)
	stats_list = []
	for c_stats in count_stats:
		#print c_stats.get_text()
		stats_list.append(c_stats.get_text())

	# 下载地址，安卓，苹果
	android_url = main_header_text.find('button',class_='btn btn-primary btn-lg android ').get('data-taptap-apk')
	print android_url
	# ios暂时没有

	# 获取开发者的话
	main_developer_text = tap_soup.find('div',class_='show-main-body collapse in first')
	developer_div = main_developer_text.find('div',id='developer-speak')
	developer_lang = developer_div.p.find_all(text=True)
	# for lang in developer_lang:
	#	print lang

	# 保存数据到字符串
	info_str = game_name + '\n' + game_company + '\n'
	for stats in stats_list:
		info_str = info_str + stats +'\t'

	info_str = info_str + '\n\n'
	info_str = info_str + '安卓下载地址：' + android_url + '\n'
	info_str = info_str + 'ios下载地址：暂无' + '\n\n'

	info_str = info_str + '开发者的话：' + '\n'
	for lang in developer_lang:
		info_str = info_str + lang + '\n'

	savefile(info_str)

	# data_list['game_name'] = game_name
	# data_list['game_company'] = game_company
	# data_list['stats_list'] = stats_list
	# data_list['android_url'] = android_url
	# data_list['developer_lang'] = developer_lang

	# analyze_data(data_list)

if __name__ == '__main__':
	get_taptap_data()



