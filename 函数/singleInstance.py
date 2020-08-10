# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     singleInstance
   Description :
   Author :       a
   date:          2019/11/11
-------------------------------------------------
"""

class Foo(object):
    def __new__(cls, name, *args, **kwargs):
        super().__new__(cls)
        if not hasattr( cls, "_instance"):
            cls._instance = super().__new__(cls)
            print("First New: %d" % id(cls._instance))
            return cls._instance
        else:
            print("Older New: ", id(cls._instance))
            return cls._instance

    def __init__(self, name, *args, **kwargs):
        super().__init__()
        if not hasattr(self, "_switch"):
            self.name = name
            print("First init: ", id(self))
            self._switch = None
        else:
            print("Older init: %d" % id(self))

f = Foo("Dragon")
f = Foo("April")
print(f.name)

