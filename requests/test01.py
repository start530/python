#!/user/bin/env python
#-*- coding:utf-8 -*-

import requests
import json

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


URL_GET = 'http://www.imooc.com'

def build_url(endpoint):
	#使用join的方法拼接url和后缀地址
	return '/'.join([URL_GET,endpoint])

def better_print(json_str):
	return json.dumps(json.loads(json_str),indent=4)

def use_simple_requests():
	response = requests.get(URL_GET)
	print ">>>Response Headers:"
	print response.headers
	print ">>>Response text:"
	response.encoding = 'utf-8'
	print response.text

def use_params_requests():
	params = {'param1': 'hello','param2': 'star'}
	response = requests.get(URL_GET, params=params)
	response.encoding = 'utf-8'
	print ">>>response headers:"
	print response.headers
	print '>>>Response Code:'
	print response.status_code
	print '>>>Response body:'
	print response.text

def request_imooc():
	headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'}
	response = requests.get(URL_GET)
	print response.encoding
	response.encoding = 'utf-8'
	print ">>>Response Code:"
	print response.status_code
	print response.text

def request_imooc_learn():
	response = requests.get(build_url('learn'))
	response.encoding = "utf-8"
	print "Response Code:"
	print response.status_code
	print response.text

if __name__ == '__main__':
	'''print ">>>use simple requests"
	use_simple_requests()
	print ">>>Use params requests"
	use_params_requests()
	'''
	print ">>>requests imooc"
	request_imooc()
	print ">>>request imooc learn"
	request_imooc_learn()