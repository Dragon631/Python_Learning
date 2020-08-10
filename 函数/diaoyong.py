# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     diaoyong
   Description :
   Author :       a
   date:          2019/10/24
-------------------------------------------------
"""

class Foo(object):
    def __init__(self):
        super(Foo, self).__init__()
        if not hasattr(self, '_switch'):
            print("--%d--", id(self))
            self._switch = None
        else:
            print("the same initial.")
            print("--%d--", id(self))
    def __new__(cls):
        super().__new__(cls)
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
            print("--%d--", id(cls._instance))
            return cls._instance
        else:
            print("the same instance.")
            print("--%d--", id(cls._instance))
            return cls._instance

f = Foo()
g = Foo()

