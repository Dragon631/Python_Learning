# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     实例012_100到200的素数
   Description :
   Author :       a
   date:          2020/5/28
-------------------------------------------------

题目
    判断101-200之间有多少个素数，并输出所有素数。

程序分析
    判断素数的方法：
    用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数
"""
import math
for i in range(100,200):
    flag=0
    for j in range(2,round(math.sqrt(i))+1):
        if i%j==0:
            flag=1
            break # 跳出j循环，从i+1开始新循环
    if flag:     # flag为真则跳过本次循环，重头开始下一次循环
        continue
 #   print(i)  # 当flag为真时，即i可被整除时，将不会执行，也就是只有素数才会执行打印操作

for i in range(101,200):
    flag = 0
    for j in range(2, 99):
       if i % j == 0 and i != j:
           flag = 1
           break
    if flag:
        continue
 #   print("素数：", i)


# for ... else ...
for i in range(100,200):
    for j in range(2,round(math.sqrt(i))+1):
        if i%j==0:
            break
    else:
        print(i)


