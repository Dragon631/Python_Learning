# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     test1
   Description :
   Author :       a
   date:          2019/4/11
-------------------------------------------------
"""

"""
class Dog(object):
    food = "gutou"
    age = "1"
    def __init__(self, name):
        self.NAME = name
    @classmethod
    def eat(self,age): #只能是类中的变量
        # print(self.NAME)
        print(age)
        print(self.food)

    @classmethod
    def eat1(self, age):  # 只能是类中的变量
        # print(self.NAME)
        age = "2"
        self.food = "tang"
    @staticmethod
    def print_1():
        print(Dog.food, Dog.age)

d = Dog("labuladuo")
d.eat(Dog.age)    #通过对象调用    1;gutou
Dog.eat(Dog.age)  #通过类调用      1;gutou
print("-----1-----")
d.eat1(Dog.age)                  # 1;tang
Dog.print_1()                    # gutou; 1
print("--------2-------")
Dog.eat1(Dog.age)                # 1; tang
Dog.print_1()                    # 1; gutou


class A(object):
    def show(self):
        print('base show')

class B(A):
    def show(self):
        print('derived show')

obj = B()
obj.show()

import abc
class magic(object,metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def run(self):
        return self + ':Run'

    @abc.abstractmethod
    def stop(self):
        return self + ':Stop'

a = magic
print(a.run('a'))
print(a.stop('a'))
print('-'*10)

class magics(magic):
    def run(self,name):
        return name + ':runnging'
    def stop(self):
        pass

b = magics()
print(b.run('浪子'))
print(b.stop('浪子'))

"""

class magic:
    """THis is a __doc__  test."""
    __user = '浪子'
    @classmethod
    def hi(cls):
        print(cls.__user)

    def __del__(self):
        print("我被回收了！")

a = magic
a.hi()

print(magic.hi())
# print(magic.__user)
# print(a.__user)
print(a._magic__user)
print(magic.__doc__)
print(a.__module__)
print(a.__class__)

a = magic()
callable(a)
# del a