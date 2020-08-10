# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     实例008_九九乘法表
   Description :
   Author :       a
   date:          2020/5/25
-------------------------------------------------
"""

for i in range(1,10):
    for j in range(i,10):
        print("%d * %d = %d" % (i, j, i * j), end="\t")
    print()

print("#" * 100)

for i in range(1,10):
    for j in range(1,i+1):
        print("%d * %d = %d" % (i, j, i * j), end="\t")
    print()

