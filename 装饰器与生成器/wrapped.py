# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     wrapped
   Description :
   Author :       a
   date:          2019/12/24
-------------------------------------------------
"""


def level(s):
    def wrapped(func):
        def inner():
            print("This is {}.".format(s))
            ret = func()
            return ret
        return inner
    return wrapped

@level("log")
def f():
    print("print test")
    return "return test..."

print(f())