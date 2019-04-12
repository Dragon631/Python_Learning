# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     生成器
   Description :
   Author :       a
   date:          2019/4/11
-------------------------------------------------
"""
# class Foo:
#     def __init__(self):
#         pass
#     def __iter__(self):
#         yield 1
#         yield 2
#         yield 3
# obj = Foo()
# for i in obj:
#     print(i)





def count(n):
	print("cunting")
	while n > 0:
		print ('before yield')
		yield n  #生成值：n
		n -= 1
		print ('after yield' )
"""
只有等到调用__next__()时才真正执行里面的语句
每次调用__next__()方法时，count函数会运行到语句yield n处为止
__next__()的返回值就是生成值n，再次调用__next__()方法时，函数继续执行yield之后的语句

上述代码在第一次调用__next__方法时，并不会打印"after yield"。
如果一直调用__next__方法，当执行到没有可迭代的值后，程序就会报错:
Traceback (most recent call last): File "", line 1, in StopIteration
所以一般不会手动的调用__next__方法，而使用for循环:
"""
# for i in count(5):
# 	print (i),



import time
"""
模拟linux系统里的tail -f 功能

def tail(file):
	t = open(file,'r')
	t.seek(0,2)  # 将指针定位到文件最后地址EOF
	while True:
		line=t.readline()
		if not line:
			time.sleep(0.1)
			continue
		yield line


for m in tail('log'):
	print(m)
"""

def tail(file, str):
	t = open(file,'r')
	t.seek(0,2)  # 将指针定位到文件最后地址EOF
	while True:
		line=t.readline()
		if not line:
			time.sleep(0.1)
			continue
		if str in line:
			yield line


for m in tail('log', 'python'):
	print(m)

"""
yield中return的作用：
作为生成器，因为每次迭代就会返回一个值，
所以不能显示在生成器函数中return 某个值，
包括None值也不行，否则会抛出“SyntaxError”的异常，
但是在函数中可以出现单独的return，表示结束该语句
"""
