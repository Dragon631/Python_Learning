# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     多装饰器
   Description :
   Author :       a
   date:          2019/4/10
-------------------------------------------------
"""


def a(func):
    print('i\'m a!')

    def e():
        print(1)
        func()
        print(2)
    return e


def b(func):
    print('i\'m b!')

    def d():
        print('a')
        func()
        print('b')

    return d


@a
@b
def c():
    print('!!!!!')

c()


"""
# f = b(a(c))
i'm b!
i'm a!
1
a
!!!!!
b
2
"""