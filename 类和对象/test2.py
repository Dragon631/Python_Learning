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

class Pizza(object):
    def __init__(self, size):
        self.size = size

    @staticmethod
    def get_size(size):
        return size

m = Pizza(20).get_size()
print(m)