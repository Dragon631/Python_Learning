# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     inner
   Description :
   Author :       a
   date:          2019/3/28
-------------------------------------------------
"""
__author__ = 'a'

def login(fun):
    def inner(money):
        print("Please input identity confirmation !")
        return fun(money)
    return inner

@login
def outCash(money):
    print("取款%s元" % money)

@login
def inCash(money):
    print("存款%s元" % money)

# outCash(100)
inCash(100)
