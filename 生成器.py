# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     生成器
   Description :
   Author :       a
   date:          2019/4/11
-------------------------------------------------
"""
class Foo:
    def __init__(self):
        pass
    def __iter__(self):
        yield 1
        yield 2
        yield 3
obj = Foo()
for i in obj:
    print(i)
