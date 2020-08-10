import threading, time

class Add(object):
	def __init__(self):
		self.lock = threading.RLock()
	def add(self, sub):
		print("%s 准备加法计算..." % threading.current_thread().name)
		try:
			self.lock.acquire()
			print("%s 先执行Sub类方法..."% threading.current_thread().name)
			time.sleep(0.01)
			sub.last()
		finally:
			self.lock.release()

	def last(self):
		try:
			self.lock.acquire()
			print("%s 进入到Add类的last方法" % threading.current_thread().name)
		finally:
			self.lock.release()
		

class Sub(object):
	def __init__(self):
		self.lock = threading.RLock()
	def sub(self, add):
		print("%s 准备减法计算..." % threading.current_thread().name)
		try:
			self.lock.acquire()
			print("%s 先执行Add类方法..." % threading.current_thread().name)
			time.sleep(0.01)
			add.last()
		finally:
			self.lock.release()
	def last(self):
		try:
			self.lock.acquire()
			print("%s 进入到Sub类的last方法" % threading.current_thread().name)
		finally:
			self.lock.release()


a = Add()
s = Sub()

def action():
	a.add(s)
	
threading.Thread(target=action).start()
s.sub(a)