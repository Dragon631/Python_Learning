# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     实例009_暂停一秒输出
   Description :
   Author :       a
   date:          2020/5/26
-------------------------------------------------
"""

import time

for i in range(10):
    date = time.ctime()
    print("time=>%s" % date)
    time.sleep(1)

# sleeptest()

for i in range(4):
    print(str(int(time.time()))[-2:])
    time.sleep(1)