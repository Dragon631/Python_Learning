# -*- coding: utf-8 -*-
# @Date_Time: 2019-07-09 17:04:47
# @File_Name: 20190709-threading.py

import threading,time

# class MyThread(threading.Thread):
# 	def __init__(self, args):
# 		self.args = args
# 		super().__init__()

# 	def run(self):
# 		time.sleep(0.01)
# 		for i in range(self.args):
# 			print('%s ---> %s' % (threading.current_thread().getName(), i))
def myThread(max):
	time.sleep(0.01)
	for i in range(max):
		print('%s ---> %s' % (threading.current_thread().getName(), i))

def main():
	print("%s started...." % (threading.current_thread().getName()))
	for i in range(100):
		print("%s count:%d" % (threading.current_thread().getName(), i))
		if i == 50:
			t1 = threading.Thread(target=myThread, args=(i,))
			t2 = threading.Thread(target=myThread, args=(i,))
			t1.daemon = True
			t2.daemon = True
			t1.start()		
			t2.start()
			# t2.join()
			# t1.join()
	print("%s stopped...." % threading.current_thread().getName())

if __name__ == '__main__':
	main()
