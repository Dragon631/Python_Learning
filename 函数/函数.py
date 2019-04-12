#!/usr/bin/env python
# -*- coding:utf-8 -*-


def foo(x,items=[]):
    items.append(x)
    return items


foo(1)
foo(2)
# print("foo_result:", foo(3))

# 结果：
# foo_result: [1, 2, 3]


def foo1(x,items=None):
    if items is None:
        items=[]
    items.append(x)
    return items


foo1(1)
foo1(2)
# print("foo1_result:", foo1(3))

# 结果：
# foo_result: [3]


def foo(w,x,y,z):
    print(w,x,y,z)

""" 关键字参数的顺序无关紧要 """
# foo(x=3,y=22,w='hello',z=[11,22,33])

""" 
位置参数和关键字参数可同时出现，但位置参数必须先出现 
等同于w='hello';x=3;y=22;z=[11,22,33]
"""
# foo('hello', 3, y=22, z=[11,22,33])

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

# a= student('April',[11,2,23],Favorite='basketball',age=20)

li = [1, 2, 3, 4, 5]
def square(items):
    for i, x in enumerate(items):
        items[i] = x * x

# square(li)
# print(li)

"""
return 语句从函数返回一个值，如果没有指定任何值或者省略return语句，
则返回None对象；如果返回值有多个，可以把它们放在一个元组中
"""
def factor(n):
    d = 2
    while (d <= (n / 2)):
        if ((n / d) * d == n):
            return ((n / d), d)
        d = d + 1
    return (n, 1)
# 将返回值放在x和y中
x, y = factor(1280)
(x, y) = factor(1280)
# print(x,y)

"""
全局变量：global语句
可放在函数体中的任何位置，并可重复使用
只有在需要修改全局变量时才必须使用它
"""

a = 1
def foo2():
    a = 2
foo2()
# print(a) # a值还是1

a1 = 1
b1 = 3
def foo3():
    global a1
    a1 = 10
    b1 = 18
foo3()
# print('a1=%d, b1=%d' % (a1, b1)) #a1值已变为10，b1不变


"""
函数嵌套
静态作用域：
python2只支持在最里层的作用域（局部变量）和全局命名空间（global）中给的变量重新赋值
即，内部函数不能给定义在外部函数中的局部变量重新赋值

解决办法：
python2: 把要修改的值放在列表或字典中
python3: 可以把n声明为nonlocal
"""

def count_down(start):
    n = {'v':start}
    def display():
        print("T-Minus:%d" % n['v'])
    def decrement():
        n['v'] -= 1
    while n['v'] > 0:
        display()
        decrement()

count_down(10)
# UnboundLocalError: local variable 'n' referenced before assignment