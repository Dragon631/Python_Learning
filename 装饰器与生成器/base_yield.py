#!/usr/bin/env python
# -*- coding:utf-8 -*-


# -*- 生成器 【案例1】-*- #
# 说明：
# 在生成器函数内部，在yield语句上出现GeneratorExit异常时就会调用close()方法
# 可以选择捕捉这个异常，以便执行清理操作。
# 以下实例：无法返回生成器迭代值
"""
# 虽然可以捕捉GeneratorExit异常，
# 但生成器函数处理异常并使用yield语句生成另一个输出值是不合法的。
# 另外，如果程序当前正在通过生成器进行迭代，
# 绝不能通过单独的执行线程或信号处理程序在该生成器上异步调用close()方法

def count_down(n):
    print("Counting down from %d" % n)

    try:
        while n > 0:
            yield n  #生成值：n
            n = n - 1
    except GeneratorExit: # 当程序执行到yield则进行异常处理
        print("Only made it to %d" % n)


n = count_down(3)

n.__next__()
# n.__next__()
# n.__next__()

"""

# -*- 协程与yield表达式 【案例2】-*- #
# 说明：
# 在函数中，yield出现在赋值运算符右边的表达式
# 此函数称为协程，它的执行是为了响应发送给它的值
"""
def receiver():
    print("Ready to receive")
    while True:
        n = (yield)
        print("Got %s" % n)

# 用例：
r = receiver()
r.__next__()    # 向前执行到第一条yield语句（必须）
r.send("What's up gays.")
r.send("What's up gays again.")

# 执行过程：
# 1.对__next__()初始调用，这是必不可少的，
#   这样协程才能执行可通过第一个yield表达式的语句，在这里协程会挂起，
#   等待相关生产器对象r的send()方法给它发送一个值
# 2.传递给send()的值由协程中的(yield)表达式返回
# 3.接收到值后，协程就会执行语句，直至遇到下一条yield语句
# 
"""

# -*- 协程与yield表达式 【案例3】-*- #
# 注意：在协程中，需要首先调用__next()__，否则很容造成错误的根源
# 因此，建议使用一个自动完成该步骤的装饰器来包装过程
"""
def coroutine(func):
    def start(*args, **kwargs):
        g = func(*args, **kwargs)
        g.__next__()
        return g
    return start

@coroutine
def receiver():
    print("Ready to receive")
    while True:
        n = (yield)
        print("Got %s" % n)


r = receiver()
r.send("hello")

# 协程的运行一般是无限期待，除非它被显式关闭或者自己退出
# 使用close()可以关闭输入值的流
r.close()
r.send('abc')
"""

# -*- 协程与yield表达式 【案例4】-*- #
# 说明：
# 如果yield表达式提供了值，协程可以使用yield语句同时接受和发出返回值
# 注：send()方法的返回值是传递给下一条yield语句的值
"""
def line_splitter(delimiter=None):
    print("Ready to split...")
    result = None
    while True:
        line = (yield result)
        result = line.split(delimiter)

# 用例：
# print("A,B,C".split(","))
s = line_splitter(",")
s.__next__()
r1 = s.send("a,b,c")
print(r1)
r2 = s.send("100,110,120")
print(r2)
"""

# -*- 列表包含 【案例5】-*- #
# 说明：
# 列表推导运算符
"""
nums = [1, 2, 3, 4, 5]
squares = [n * n for n in nums]
for i in squares:
    print(i)
'''
列表推导的一般语法：
[expression for item1 in iterable1 if condition1
            for item1 in iterable1 if condition1
            ...
            for item1 in iterable1 if condition1]

这种语法大致上等价于以下代码：
s = []
for item1 in iterable1:
    if condition1:
        for item2 in iterable2:
            if condition2:
                ...
                for itemN in iterableN:
                    if conditionN: s.append(expression)
'''

"""

# -*- 列表包含 【案例6】-*- #
# 说明：
# 列表推导运算符
"""
a = [1, 2, 3, 4 ,5]
r = [ x for x in a]
print(x) # 在python2 中迭代变量x仍保留a最后一项的值，x被设置为5
         # 在python3 中迭代变量一直都是私有变量，不存在这种情况
"""

# -*- 生成器表达式 【案例7】-*- #
# 说明：
# 生成器表达式是一个对象，类似于列表，但要用圆括号代替方括号
# 它会创建一个通过迭代并按照需要生产值的生成器对象
"""
a = [1, 2, 3 ,4]
b = (10*i for i in a)

print(b)
#<generator object <genexpr> at 0x0000000001E23228>
print(b.__next__())
print(b.__next__())
print(b.__next__())
"""

# -*- 生成器表达式 【案例8】-*- #
# 说明：
# 与列表推导不同，生成器表达式不会创建序列形式的对象
# 不能对它进行索引，也不能进行任何常规的列表操作，如append()
# 但是，使用内置的list()函数可以将生成器表达式转换为列表

"""
with open("test.sh",'r') as f:
    lines = (t.strip() for t in f)
    comments = (t for t in lines if t[0:1] == "#")  # 因为使用"GBK"编号，所以每个字符占用两个字节
    # clist = list(comments) # 转换为list列表
    for c in comments:
        print(c)

    # print("#"*30)
    #
    # for l in clist:
    #     print(l)
"""
