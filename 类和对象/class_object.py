#!/usr/bin/env python
# -*- coding:utf-8 -*-


# -*- class 【案例1】-*- #
# 说明：
# 类 = 函数（方法）+ 变量（类变量） + 计算出的属性（特性） 组成的集合
# 类仅设置将在以后创建的所有实例都使用的属性
# 在__init__()内，通过将属性分配给self来将其保存到实例中
# 点（.）运算符用于属性绑定，通过点运算符访问相关属性
"""
class Account(object):
    num_accounts = 0 # 类变量是可在所有实例之间共享的值
    def __init__(self, name, balance):

        self.name = name
        self.balance = balance
        Account.num_accounts += 1
    def __del__(self):
        Account.num_accounts -= 1
    def deposit(self, amt):
        self.balance = self.balance + amt
    def withdraw(self, amt):
        self.balance = self.balance - amt
    def inquiry(self):
        return self.balance

a = Account("April",1000.00)
b = Account("Bill",100.00)
print(a.name)

"""


# -*- class 【案例2】-*- #
# 说明：范围规则
# 类 = 函数（方法）+ 变量（类变量） + 计算出的属性（特性） 组成的集合
# 类仅设置将在以后创建的所有实例都使用的属性
# 在__init__()内，通过将属性分配给self来将其保存到实例中
# 点（.）运算符用于属性绑定，通过点运算符访问相关属性
""" 
class Account(object):
    num_accounts = 0 # 类变量是可在所有实例之间共享的值
    def __init__(self, name, balance):

        self.name = name
        self.balance = balance
        Account.num_accounts += 1
    def __del__(self):
        Account.num_accounts -= 1
    def deposit(self, amt):
        self.balance = self.balance + amt
    def withdraw(self, amt):
        self.balance = self.balance - amt
    def inquiry(self):
        return self.balance

a = Account("April",1000.00)
b = Account("Bill",100.00)
print(a.name)
"""

# -*- class 【案例3】-*- #
# 说明：范围规则
"""
class room:
    def __init__(self,area=120,usedfor='sleep'):
        self.area = area
        self.usedfor = usedfor

    def display(self):
        print("this is my house")

class babyroom(room):
    def __init__(self,area=40,usedfor="son",wallcolor='green'):
        super().__init__(area, usedfor)
        self.wallcolr = wallcolor

    def display(self):
        super().display()
        print("babyroom area:%s wallcollor:%s" % (self.area,self.wallcolr))

class rent:
    def __init__(self,money=1000):
        self.rentmoney = money

    def display(self):
        print("for rent at the price of %s"%self.rentmoney)

class agent(babyroom,rent):
# class agent(rent,babyroom):
    def display(self):
        super().display()
        print("rent house agent")

agent().display()

# 结果：
# this is my house # 调用root(babyroom.diaplay())
# babyroom area:40 wallcollor:green
# rent house agent
"""

# -*- class 【案例4】-*- #
# 说明：范围规则
# 方法和属性的调用
import requests

class cc:
    ccc = 'ccc'
    # cc就是类名 如果想要继承别的类 就class cc(threading) 意思就是从threading继承
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        # 定义构造的过程就是实例化
    def runx(self):
        print(self.a*10)
        print(self.b*5)
        print(self.c*2)
    def runy(self):
        print(requests.get('http://www.langzi.fun').headers)
e = cc('AAA','CCC','EEE')
e.runx()
e.runy()
# 这两个就是调用类里面的方法
print(e.c)
#实例变量指的是实例本身拥有的变量。每个实例的变量在内存中都不一样。
print(e.ccc)
#类变量，在类里面找到定义的变量。