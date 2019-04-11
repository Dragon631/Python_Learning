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


def wrapper_out1(func):
    print('--out11--')

    def inner1(*args, **kwargs):
        print("--in11--")
        ret = func(*args, **kwargs)
        print("--in12--")
        return ret

    print("--out12--")
    return inner1


def wrapper_out2(func):
    print('--out21--')

    def inner2(*args, **kwargs):
        print("--in21--")
        ret = func(*args, **kwargs)
        print("--in22--")
        return ret

    print("--out22")
    return inner2


@wrapper_out2
@wrapper_out1
def test():
    print("--test--")
    return 1 * 2


if __name__ == '__main__':
    test()


"""
--out11--
--out12--
--out21--
--out22--
--in21--
--in11--
--test--
--in12--
--in22--
"""