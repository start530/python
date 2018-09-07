#!/user/bin/env python
#-*- coding:utf-8 -*-

__author__ = "star"
'''download img test
'''

import requests
import json

URL_GET = 'http://www.imooc.com'

def build_url(endpoint):
	#使用join的方法拼接url和后缀地址
	return '/'.join([URL_GET,endpoint])

def better_print(json_str):
	return json.dumps(json.loads(json_str),indent=4)

def download_image():
	'''下载图片
	'''
	img_url = 'https://gju1.alicdn.com/tps/TB21hMCkBjTBKNjSZFDXXbVgVXa-1072935401.jpg_400x400Q90.jpg'
	headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'}
	response = requests.get(img_url,headers=headers,stream=True)
	print ">>>hhaha"
	print response.status_code,response.reason
	print response.headers

	with open('demo.jpg','wb') as fd:
		for chunk in response.iter_content(128):
			fd.write(chunk)

if __name__ == '__main__':
	download_image()