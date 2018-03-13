#-*- coding:utf-8 -*-

'check user passwd is right'
__author__ = 'star'

import os
import json
import hashlib

def checkPwd(username,pwd):
    f = open('userInfo.txt','r')
    db = json.loads(f.read())
    f.close()

    if db.has_key(username) == False:
        print 'user file not has user:',username
        return
    else:
        #计算输入的用户md5的值
        md5 = hashlib.md5()
        md5.update(pwd.encode('utf-8'))
        pwd_md5 = md5.hexdigest()

        #获取数据表中该用户密码md5值
        user_pwd_md5 = db[username]
        if user_pwd_md5 == pwd_md5:
            print "user passwd is correct"
        else:
            print "user passwd is wrong"

username = raw_input("please input user name:")
passwd = raw_input("please input passwd:")
checkPwd(username,passwd)
