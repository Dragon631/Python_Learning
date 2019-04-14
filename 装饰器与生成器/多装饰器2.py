# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     多装饰器
   Description :
   Author :       a
   date:          2019/4/10
-------------------------------------------------
"""


def decorator_a(func):
    print('函数a_1')

    def inner_a(*args, **kwargs):
        print('函数a_2')
        return func(*args, **kwargs)

    return inner_a


def decorator_b(func):
    print('函数b_1')

    def inner_b(*args, **kwargs):
        print('函数b_2')
        return func(*args, **kwargs)

    return inner_b


def decorator_c(func):
    print('函数c_1')

    def inner_a(*args, **kwargs):
        print('函数c_2')
        return func(*args, **kwargs)

    return inner_a


def decorator_d(func):
    print('函数d_1')

    def inner_a(*args, **kwargs):
        print('函数d_2')
        return func(*args, **kwargs)

    return inner_a


# 当有多个装饰器时， 从下到上调用装饰器；
@decorator_d
@decorator_c
@decorator_b
@decorator_a
def f(x):
    print('Get in f')
    return x * 2


f(1)
