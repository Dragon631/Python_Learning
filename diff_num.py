# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     diff_num
   Description :
   Author :       a
   date:          2019/4/3
-------------------------------------------------
"""
__author__ = 'a'

for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if (i != j) and (j != k) and (i!= k):
                print(i,j,k,)