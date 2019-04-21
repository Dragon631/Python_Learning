# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     test
   Description :
   Author :       a
   date:          2019/4/21
-------------------------------------------------
"""
def fun():
    print("start...")
    m = yield
    print(m)
    print('middle...')
    n = yield
    print(n)
    print('end...')

a = fun()
a.__next__()
a.send(1)
a.send(2)
# a.send("message")
# a.send("aa")
# a.__next__()
