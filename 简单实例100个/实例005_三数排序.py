# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     实例005_三数排序
   Description :
   Author :       a
   date:          2020/5/21
-------------------------------------------------

题目:
    输入三个整数x,y,z，请把这三个数由小到大输出
"""

# a = int(input("a="))
# b = int(input("b="))
# c = int(input("c="))

li = []
for i in range(3):
    a = int(input("input %d:" % (i)))
    li.append(a)

for i in range(len(li)):
    for j in range(i, len(li)):
        if li[i] > li[j]:
            li[i], li[j] = li[j], li[i]
print(li)