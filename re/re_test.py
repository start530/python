#!/user/bin/env python
# -*- coding:utf-8 -*-

import re


def is_valid_email(addr):
    re_mail = r'[0-9a-zA-Z\.]+\@[0-9a-zA-Z]+.com$'
    if re.match(re_mail, addr):
        print '%s is mail address' % addr
        return True
    else:
        print '%s is wrong mail address' % addr
        return False


if __name__ == '__main__':
    is_valid_email('hyltk1314@163.com')
    is_valid_email('451618148@qq.com')
    is_valid_email('/%23@qw.com')
    is_valid_email('star.hzk@163.com')

