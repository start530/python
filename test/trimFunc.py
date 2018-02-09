# -*- coding: utf-8 -*-

star = " star is so cool "
print(star)

def trim(s):
    if s[:1] == " ":
        s = s[1:]
    if s[-1:] == " ":
        s = s[:-1]
    
    return s

print(trim(star))
