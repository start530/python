#-*- coding:utf-8 -*-

'get hash code from str and write to file'
__author__ = 'star'

import os
import hashlib
import json

def write_hash_tofile(pas):
    my_md5 = hashlib.md5()
    my_md5.update(pas.encode('utf-8'))
    pas_md5 = my_md5.hexdigest()
    print pas,'md5 = ',pas_md5
    
    #获取保存用户数据的字典
    f = open('userInfo.txt','r')
    userInfo_str = f.read()
    db = {}
    if len(userInfo_str) != 0:
    	db = json.loads(userInfo_str)
    f.close()

    if len(db) == 0:
    	print "user file is empty!"
    	dic = {pas:pas_md5}
    	ff = open('userInfo.txt','w')
    	ff.write(json.dumps(dic))
    	ff.close()
    	return

    if db.has_key(pas) == False:
    	db[pas] = pas_md5
    	ff = open('userInfo.txt','w')
    	ff.write(json.dumps(db))
    	ff.close()
    else:
    	print "already had keys:",pas

#input
user_name = raw_input("please input user name:")
write_hash_tofile(user_name)

