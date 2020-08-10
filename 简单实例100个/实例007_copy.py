# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     实例007_copy
   Description :
   Author :       a
   date:          2020/5/23
-------------------------------------------------
题目
    将一个列表的数据复制到另一个列表中

程序分析
    字典与列表是可变对象，可以任意调用copy模块
"""

# copy and deepcopy

import copy

server = {"mem":[10, 80], "cpu":[1,32], "hdd":[100,1000]}

server1 = copy.copy(server)
server2 = copy.deepcopy(server)

print("server1_shallow:", server1)
print("server2_deep:", server2)
print("server:", server)
server["mem"][1] = 90
server["sata"] = [100, 200]

print("\nserver1_shallow:", server1)
print("server2_deep:", server2)
print("server:", server)

