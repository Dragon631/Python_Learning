# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     冒泡排序
   Description :
   Author :       a
   date:          2019/4/1
-------------------------------------------------
"""
__author__ = 'a'

#冒泡法排序
#首先找出所有值中，值最大的排到最后位置
#即：后面的值，跟前面的比较，值大的往后移
def bubble(args):

    for i in range(1, len(args) - 1):
        for j in range(len(args) - i):
            if args[j] > args[j + 1]:
                args[j], args[j + 1] = args[j + 1], args[j]
    print(args)

data = [1, 5, 33, 80, 2, 7, 8, 55, 3, 90,11]
bubble(data)