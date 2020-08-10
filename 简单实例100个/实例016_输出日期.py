# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     实例016_输出日期
   Description :
   Author :       a
   date:          2020/6/4
-------------------------------------------------

题目
    输出指定格式的日期

程序分析
    使用 datetime 模块

"""

import datetime

print(datetime.datetime.now())
print(datetime.date.today())
print(datetime.date.today().strftime('%d/%m/%Y'))
print(datetime.date(2020,6,9))
day = datetime.date(2020,6,9)
day = day.replace(year=(day.year + 22), month=day.month+1, day=(day.day + 1))
print(day)