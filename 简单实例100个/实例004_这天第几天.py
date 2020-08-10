# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     实例004_这天第几天
   Description :
   Author :       a
   date:          2020/5/20
-------------------------------------------------
题目:
    输入某年某月某日，判断这一天是这一年的第几天？
    闰年分为普通闰年和世纪闰年
        普通闰年:公历年份是4的倍数的，且不是100的倍数，为普通闰年。（如2004年就是闰年）
        世纪闰年:公历年份是整百数的，必须是400的倍数才是世纪闰年（如1900年不是世纪闰年，2000年是世纪闰年）
"""


def isLeapYear(args):
    if ((args % 4 == 0 and args % 100 != 0) or args % 400 == 0) :
        return True
    else :
        return False

days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]

year = int(input("Please input year: "))
month = int(input("Please input month: [1-12]"))
day = int(input("Please input day: [1-31]"))
n = 0
if isLeapYear(year):
    days[2] += 1

for i in range(month):
    n += days[i]

print("%d月%d日是%d年的第%d天！" % (month, day, year, n + day))
