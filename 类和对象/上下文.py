# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     上下文
   Description :
   Author :       a
   date:          2019/4/11
-------------------------------------------------
"""
__author__ = 'a'

"""
# 方法一：begin
class Wallet(object):
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('%s open the wallet carefully.' % self.name)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('%s put the wallet away sadly.' % self.name)


def usedMoney(name):
    return Wallet(name)

with usedMoney('April') as used:
    print('Spend out $500.')
# 方法一：end
"""

"""
# 方法二：begin
class Wallet(object):
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('%s open the wallet carefully.' % self.name)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('%s put the wallet away sadly.' % self.name)

    def used_money(self, money):
        print('%s spend out %s dollar.' %(self.name, money))


with Wallet('April') as w:
    w.used_money(500)
# 方法二：end
"""

# 方法三：begin
import  contextlib

@contextlib.contextmanager
def used_money(name):
    try:
        print('%s put the wallet away sadly.' % name)
        yield None
    finally:
        print('%s put the wallet away sadly.' % name)


with used_money('April') as u:
    print('Spend out 500 dollars.')
