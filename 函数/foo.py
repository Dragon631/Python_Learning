#!/usr/bin/env python
# -*- coding:utf-8 -*-

class A(object):
    def __init__(self, *args, **kwargs):
        print("Call __init__ from %s" % self.__class__)

    def __new__(cls, *args, **kwargs):
        obj = object.__new__(cls, *args, **kwargs)
        print("Call __new__ from %s" % obj.__class__)
        return obj


class B(object) :
    def __init__(self, *args, **kwargs) :
        print("Call __init__ from %s" % self.__class__)

    def __new__(cls, *args, **kwargs) :
        obj = object.__new__(A, *args, **kwargs)
        print("Call __new__ from %s" % obj.__class__)
        return obj

class OneInstance(object):
    def __new__(cls, *args, **kwargs):
        super().__new__(cls, *args, **kwargs)
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls, *args, **kwargs)
            print("new:---%s---" % id(cls._instance))
            return cls._instance
        else:
            print("New same: ---%s---" % id(cls._instance))
            return cls._instance

    def __init__(self, *args, **kwargs):
        super().__init__()
        if not hasattr(self, "_switch"):
            print("init:---%s---" % id(self))
            self._switch = None
        else:
            print("init has initailled ---%s---" % id(self))


b = B()
print(type(b))
a = A()
#
# one = OneInstance()
# two = OneInstance()

class TestException(object):
    try:
        # 19/0
        open('text.txt', 'r')
    except Exception as ret:
        print("Error: ", ret)
t = TestException()
