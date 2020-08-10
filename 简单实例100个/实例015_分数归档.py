# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     实例015_分数归档
   Description :
   Author :       a
   date:          2020/6/3
-------------------------------------------------

题目
    利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示

"""

score = float(input("input the score: "))

# if score >= 90:
#     print("Get A Score.")
# elif score >= 60 and score < 90:
#     print("Get B Score.")
# else:
#     print("Get C Score.")


points=int(input('输入分数：'))
if points>=90:
    grade='A'
elif points<60:
    grade='C'
else:
    grade='B'
print(grade)