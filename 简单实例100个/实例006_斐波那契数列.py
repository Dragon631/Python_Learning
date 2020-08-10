# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     实例006_斐波那契数列
   Description :
   Author :       a
   date:          2020/5/22
-------------------------------------------------

题目
    斐波那契数列（Fibonacci sequence）

程序分析
    斐波那契数列指的是这样一个数列：1、1、2、3、5、8、13、21、34、……
    这个数列从第3项开始，每一项都等于前两项之和
    图方便就递归实现，图性能就用循环
"""


# 递归
def Fib(n):
    return 1 if n <= 2 else Fib(n-1) + Fib(n-2)
print(Fib(int(input("请输入数值："))))


# 循环
num = int(input("请输入数值："))
ret = 0
a, b = 1, 1
print(a,b)
for i in range(num - 1):
    a, b = b, a + b
    print(a,b)
