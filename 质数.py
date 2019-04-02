# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     质数
   Description :
   Author :       a
   date:          2019/4/1
-------------------------------------------------
"""
__author__ = 'a'
#找出数值以内的所有质数

def primeNum(args):
    prime = []
    for i in range(2, args+1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            prime.append(i)
    print(prime)

primeNum(97)