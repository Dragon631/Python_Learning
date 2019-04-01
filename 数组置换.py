# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     数组置换
   Description :
   Author :       a
   date:          2019/3/29
-------------------------------------------------
"""
__author__ = 'a'

"""
-------------------------
|(0,0)|(0,1)|(0,2)|(0,3)|
-------------------------
|(1,0)|(1,1)|(1,2)|(1,3)|
-------------------------
|(2,0)|(2,1)|(2,2)|(2,3)|
-------------------------
|(3,0)|(3,1)|(3,2)|(3,3)|
-------------------------
(i,j)=>
i = 0, j = 0,1,2,3
i = 1, j = 1,2,3
i = 2, j = 2,3
i = 3, j = 3 # j = 3 可省略
"""
# 方法一：
#
def vdisplay(args):
    for i in range(len(args)-1):
        for j in range(i, len(args)):
            args[i][j], args[j][i] = args[j][i], args[i][j]
            # print(args)
    return args

rect = [[1, 2, 3, 4], ['a', 'b', 'c', 'd'], [5, 6, 7, 8], ['e', 'f', 'g', 'h']]
result = vdisplay(rect)
for r in result:
    print(r)

# 方法二：
rect1 = [[1, 2, 3, 4], ['a', 'b', 'c', 'd'], [5, 6, 7, 8], ['e', 'f', 'g', 'h']]

# row[i]实现将取出列值，放到一个列表中，实现行列对换
x = [[row[i] for row in rect1] for i in range(len(rect1))]  # 90°转置
for varr1 in x:
    print(varr1)


