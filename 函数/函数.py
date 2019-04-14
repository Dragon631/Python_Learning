#!/usr/bin/env python
# -*- coding:utf-8 -*-


#>**************************【案例一】****************************<#
# 默认参数保留了前面调用进行的修改
"""
def foo(x,items=[]):
    items.append(x)
    return items


foo(1)
foo(2)
print("foo_result:", foo(3))

# 结果：
# foo_result: [1, 2, 3]
"""


#>**************************【案例二】****************************<#
# 使用None值避免默认参数保留了前面调用进行修改的影响
"""
def foo1(x,items=None):
    if items is None:
        items=[]
    items.append(x)
    return items


foo1(1)
foo1(2)
print("foo1_result:", foo1(3))

# 结果：
foo_result: [3]
"""


#>**************************【案例三】****************************<#
"""
def foo(w,x,y,z):
    print(w,x,y,z)

# 关键字参数的顺序无关紧要
foo(x=3,y=22,w='hello',z=[11,22,33])

# 位置参数和关键字参数可同时出现，但位置参数必须先出现 
# 等同于w='hello';x=3;y=22;z=[11,22,33]

foo('hello', 3, y=22, z=[11,22,33])

#foo(3, 22, w='hello', z=[11,22,33])
# 不能多次定义参数值
# 位置参数w以提供了数值3，后面再次赋值w='hello'
"""


#>**************************【案例四】****************************<#
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


#>**************************【案例五】****************************<#
"""
# 接受数量不定的位置或关键字参数
# args是一个位置参数的元组
# kwargs是一个关键字参数的字典

def student(*args, **kwargs):

    name = args
    other = kwargs
    print(name,other)

# a= student('April',[11,2,23],Favorite='basketball',age=20)

li = [1, 2, 3, 4, 5]
def square(items):
    for i, x in enumerate(items):
        items[i] = x * x

square(li)
print(li)
"""


#>**************************【案例六】****************************<#
"""
# return 语句从函数返回一个值，如果没有指定任何值或者省略return语句，
# 则返回None对象；如果返回值有多个，可以把它们放在一个元组中

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


#>**************************【案例七】****************************<#
"""
# 全局变量：global语句
# 可放在函数体中的任何位置，并可重复使用
# 只有在需要修改全局变量时才必须使用它

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


#>**************************【案例八】****************************<#
"""
# 函数嵌套
# 静态作用域：
# python2只支持在最里层的作用域（局部变量）和全局命名空间（global）中给的变量重新赋值
# 即，内部函数不能给定义在外部函数中的局部变量重新赋值

# 以下是失败案例
def count_down(start):
    n = start
    def display():
        print("T-Minus:%d" % n)
    def decrement():
        n -= 1
    while n > 0:
        display()
        decrement()

count_down(10)

# 报错：UnboundLocalError: local variable 'n' referenced before assignment
# 解决办法：
# python2: 把要修改的值放在列表或字典中
# python3: 可以把n声明为nonlocal

"""


#>**************************【案例九】****************************<#
"""
# 字典变量

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
"""


#>**************************【案例十】****************************<#
"""
# 列表变量
def count_down(start):
    n = [start]
    def display():
        print("T-Minus:%d" % n[0])
    def decrement():
        n[0] -= 1
    while n[0] > 0:
        display()
        decrement()

count_down(10)
"""


#>**************************【案例十一】****************************<#
"""
# nonlocal声明
# nonlocal声明不会把名称绑定到任意函数中定义的局部变量
# 而是搜索当前调用栈中的下一层函数定义，即动态作用域

def count_down(start):
    n = start
    def display():
        print("T-Minus:%d" % n)
    def decrement():
        nonlocal n   # 绑定到外部的变量n
        n -= 1
    while n > 0:
        display()
        decrement()

count_down(10)
"""


#>**************************【案例十二】****************************<#
# 使用没有赋值的局部变量，将抛出 UnboundLocalError异常
"""
i = 0
def foo():
    i = i + 1
    print(i)

foo()
# 结果：UnboundLocalError: local variable 'i' referenced before assignment
"""


#>**************************【案例十三】****************************<#
# 函数在python中是第一类对象，即可以当成其他函数的参数或返回值
"""
def foo(fun):
    return fun

def hello_world():
    return 'Hello World!'

f = foo(hello_world()) # 传递一个函数做为参数
print(f)
"""


# -*- 闭包 -*-【案例十四】*******************************************<#
# 1.闭包是由函数及其相关的引用环境组合而成的实体(即：闭包=函数+引用环境)
# 2.在一个函数内部可以定义另一个函数，有了嵌套函数这种结构，便会产生闭包问题
# 3.如果在一个内部函数里，对在外部作用域（但不是在全局作用域）的变量进行引用，
# 那么内部函数就被认为是闭包(closure)
# 4.由于闭包把函数和运行时的引用环境打包成为一个新的整体，
# 所以就解决了函数编程中的嵌套所引发的问题
"""
import foo
'''
foo.py
x = 1111
def callf(fun):
    return fun()
'''

x = 21
def hello_world():
    return 'Hello %d' % x

f = foo.callf(hello_world) # x调用的是hello_world函数自己的变量
print(f)

print(hello_world.__globals__)
"""


#>**************************【案例十五】****************************<#
# 闭包和嵌套的应用：惰性求值（lazy evaluation）/延迟求值的代码
"""
# from urllib import urlopen        # python2.x
from urllib.request import urlopen  # python3.x

# page实际上并不执行任何有意义的计算
# 仅创建和返回函数get()，获取web页面的内容
# get()函数中执行的计算实际上延迟到了程序后面对get()求值的时候
# 如果需要在一系列函数调用中保持某个状态，使用闭包是一个非常高效的方式

def page(url):
    def get():
        return urlopen(url).read()
    return get

python = page("http://www.python.org")
jython = page("http://www.jython.org")

print(python)
print(jython)

print(python.__closure__)

print(python.__closure__[0].cell_contents)
print(jython.__closure__[0].cell_contents)

# pydata = python()
# jydata = jython()
#
# print(pydata)
# print(jydata)

"""


# -*- 闭包 -*-【案例十六】*******************************************<#
# 简单演示，infun就是闭包，是个独立的实例，其m值与exfun是隔离的
"""
def exfun():
    m = 11
    print(m)
    def infun():
        m = 22
        print(m)

    infun()
    print(m)

f = exfun()
"""


# -*- 闭包 -*-【案例十七】*******************************************<#
# 简单函数和定义说明闭包
"""
def addx(x):
    def adder(y):
        return x + y
    return adder

s = addx(10)  # return adder
print(s.__name__)# adder

e = s(12)  # adder(12)
print(e)

# 说明：
# adder(y)这个内部函数，
# 对在外部作用域（但不是在全局作用域）的变量进行引用：
# x就是被引用的变量，x在外部作用域addx里面，但不在全局作用域里，
# 则这个内部函数adder就是一个闭包
# 闭包=函数块+定义函数时的环境：adder就是函数块，x就是环境

"""


# -*- 闭包 -*-【案例十八】*******************************************<#
# 注意：闭包中是不能修改外部作用域的局部变量的
"""
def foo():
    a = 1
    def bar():
        a = a + 1
        return a
    return bar

f = foo()
print(f())

# 报错：UnboundLocalError: local variable 'a' referenced before assignment

# 这是因为在执行代码 c = foo()时，python会导入全部的闭包函数体bar()来分析其的局部变量，
# python规则指定所有在赋值语句左面的变量都是局部变量，
# 则在闭包bar()中，变量a在赋值符号"="的左面，被python认为是bar()中的局部变量。
# 再接下来执行print(c())时，程序运行至a = a + 1时，因为先前已经把a归为bar()中的局部变量，
# 所以python会在bar()中去找在赋值语句右面的a的值，结果找不到，就会报错
"""


# -*- 闭包 -*-【案例十九】*******************************************<#
# 用途1，当闭包执行完后，仍然能够保持住当前的运行环境
# 比如说，如果你希望函数的每次执行结果，都是基于这个函数上次的运行结果
# 用途2，闭包可以根据外部作用域的局部变量来得到不同的结果，这有点像一种类似配置功能的作用
# 我们可以修改外部的变量，闭包根据这个变量展现出不同的功能
# 比如，有时我们需要对某些文件的特殊行进行分析，先要提取出这些特殊行
"""
def make_filter(keep):
    def the_filter(file_name):
        file = open(file_name)
        lines = file.readlines()
        file.close()
        filter_doc = [i for i in lines if keep in i]
        return filter_doc
    return the_filter

# 如果我们需要取得文件"result.txt"中含有"pass"关键字的行，则可以这样使用例子程序

filter = make_filter("pass")  
filter_result = filter("result.txt")
"""


# -*- 闭包 -*-【案例二十】*******************************************<#
"""
def count_down(n):
    def next():
        nonlocal n
        r = n
        n -= 1
        return r
    return next

# 用例
next = count_down(10)
while True:
    v = next() # 获取下一个值
    if not v: break
    print(v)

"""


