# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     递归
   Description :
   Author :       a
   date:          2019/3/29
-------------------------------------------------
"""
__author__ = 'a'

def recursive(args):
    result = args/2
    print(result)
    if result > 1:
        return recursive(result)




recursive(100)
