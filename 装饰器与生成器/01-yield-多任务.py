# -*- coding: utf-8 -*-
# @Date_Time: 2019-06-12 16:00:14
# @Path_File: E:\Python_Data\Projects\Python_Learning\装饰器与生成器\01-yield-多任务.py

def test1():
	count = 0
	while count < 10:
		count += 1
		yield
		print("---test1---")		

def test2():
	count = 0
	while count < 10:
		count += 1
		yield
		print("---test2---")	

def main():
	t1 = test1()
	t2 = test2()
	while True:
		try:
			t1.__next__()
			t2.__next__()
		except StopIteration:
			print("end")
			break
if __name__ == '__main__':
	main()