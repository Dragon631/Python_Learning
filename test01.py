# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     test01
   Description :
   Author :       a
   date:          2019/3/26
-------------------------------------------------
"""
__author__ = 'a'

""" 格式化字符串 """

s1 = "{0} is {1} years old."
s2 = "{name} is {age} years old."
d1 = {'name': 'Jack', 'age': 28}
r1 = s1.format('Lily', 25)
r2 = s2.format(**d1)

print(r1, r2)
