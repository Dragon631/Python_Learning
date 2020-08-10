# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     多装饰器3
   Description :
   Author :       a
   date:          2019/4/10
-------------------------------------------------
"""
__author__ = 'a'


def wrapper_A(func):
    print('--A1--')

    def inner1(*args, **kwargs):
        print("--11--")
        ret = func(*args, **kwargs)
        print("--12--")
        return ret

    print("--A2--")
    return inner1


def wrapper_B(func):
    print('--B1--')

    def inner2(*args, **kwargs):
        print("--21--")
        ret = func(*args, **kwargs)
        print("--22--")
        return ret

    print("--B2")
    return inner2


@wrapper_B
@wrapper_A
def test():
    print("--test--")
    return 1 * 2


if __name__ == '__main__':
    # test()
    print(test())


"""
--A1--
--A2--
--B1--
--B2
--21--
--11--
--test--
--12--
--22--
2
"""