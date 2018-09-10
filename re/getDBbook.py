#!/user/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'star'
'''get douban book list and use re
'''

import re
import requests
import os
import sys
from bs4 import BeautifulSoup



reload(sys)
sys.setdefaultencoding('utf-8')

DB_URL = "https://book.douban.com"


def get_dbinfo_by_regular():
    # 通过正则表达式获取豆瓣页面数据
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
    response = requests.get(DB_URL, headers=header)
    content = response.text

    # 正则表达式
    #pattern = re.compile('<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>.*?publisher">(.*?)</span>.*?</li>', re.S)
    # = re.findall(pattern, content)

    pattern = re.compile('<li.*?"cover">.*?href="(.*?)"\s+title="(.*?)">', re.S)
    results = re.findall(pattern, content)
    print(results)

    for result in results:
        print result[0]
        print result[1]


def get_dbinfo_by_bs4():
    # 通过beautifulsoup解析豆瓣页面数据
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
    response = requests.get(DB_URL, headers=header)
    content = response.text

    soup = BeautifulSoup(content, 'lxml')
    print soup.title
    print type(soup.title)
    print soup.prettify()
   # print soup
    book_list = soup.find_all('div', class_='cover')
    print book_list

    for book in book_list:
        at = book.find_all('a')
        for tt in at:
            bookN = tt.get('title')
            if bookN != None:
                print bookN



      #  print book
      #  book_title = book.a.attrs['title']
      #  print book_title



if __name__ == '__main__':
    # get_douban_book()
    get_dbinfo_by_bs4()




