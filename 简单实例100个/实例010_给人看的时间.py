# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     实例010_给人看的时间
   Description :
   Author :       a
   date:          2020/5/27
-------------------------------------------------
"""

import time

for i in range(5):
    t = time.strftime("%Y-%m-%d %p %H:%M:%S", time.localtime())
    time.sleep(1)
    print(t)

