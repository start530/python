#-*- coding -*-

'url lib test'
__author__ = 'star'

from urllib import request
import json

def fetch_date(url):
    with request.urlopen(url) as f:
        data = f.read()
        json_data = json.loads(data)
        print json_data

fetch_date('www.baidu.com')
