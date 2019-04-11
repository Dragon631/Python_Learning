#!/usr/bin/env python
# -*- coding:utf-8 -*-


def foo(x,items=[]):
    items.append(x)
    return items


foo(1)
foo(2)
print("foo_result:", foo(3))

# 结果：
# foo_result: [1, 2, 3]


def foo1(x,items=None):
    if items is None:
        items=[]
    items.append(x)
    return items


foo1(1)
foo1(2)
print("foo1_result:", foo1(3))

# 结果：
# foo_result: [3]


def foo(w,x,y,z):
    print(w,x,y,z)

""" 关键字参数的顺序无关紧要 """
foo(x=3,y=22,w='hello',z=[11,22,33])

""" 
位置参数和关键字参数可同时出现，但位置参数必须先出现 
等同于w='hello';x=3;y=22;z=[11,22,33]
"""
foo('hello', 3, y=22, z=[11,22,33])

""" 
foo(3, 22, w='hello', z=[11,22,33])
# 不能多次定义参数值
# 位置参数w以提供了数值3，后面再次赋值w='hello'
"""

"""
# 没搞懂，以下说明**参数的实现
def make_table(data, **parms):
    fgcolor = parms.pop("fgcolor","black")
    bgcolor = parms.pop("bgcolor","white")
    width = parms.pop("width", None)

    if parms:
        raise TypeError("Unsupported configuration options %s" %list(parms))

make_table(items, fgcolor="black",bgcolor="white",border=1, borderstyle="grooved", collpadding=10,width=400)
"""

"""
接受数量不定的位置或关键字参数
args是一个位置参数的元组
kwargs是一个关键字参数的字典
"""
def student(*args, **kwargs):

    name = args
    other = kwargs
    print(name,other)

a= student('April',[11,2,23],Favorite='basketball',age=20)

li = [1, 2, 3, 4, 5]
def square(items):
    for i, x in enumerate(items):
        items[i] = x * x

square(li)
print(li)