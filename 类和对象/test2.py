# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     test2
   Description :
   Author :       a
   date:          2019/4/11
-------------------------------------------------
"""
__author__ = 'a'

# class Pizza(object):
#     def __init__(self, size):
#         self.size = size
#
#     @staticmethod
#     def get_size(size):
#         return size
#
# m = Pizza(20).get_size()
# print(m)


import gc

class ClassA():
    pass
    def __del__(self):
        print('object born,id:%s'%str(hex(id(self))))

gc.set_debug(gc.DEBUG_LEAK)
a = ClassA()
b = ClassA()

a.next = b
b.prev = a

print("--1--")
print(gc.collect())
print("--2--")
del a
print("--3--")
del b
print("--3-1--")
print(gc.collect())
print("--4--")