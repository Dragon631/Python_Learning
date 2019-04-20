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