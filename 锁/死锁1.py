import threading
import time

class MyThreadA(threading.Thread):
	def run(self):
		lock.acquire()
		try:
			global i
			i += 1
			print("[%s]---A1---，value:%d" % (threading.current_thread().name, i))
			time.sleep(0.05)
		finally:
			lock.release()

class MyThreadB(threading.Thread):
	def run(self):
		lock.acquire()
		try:
			global i
			i += 1
			print("[%s]---B1---，value:%d" % (threading.current_thread().name, i))
			time.sleep(0.05)
		finally:
			lock.release()

lock = threading.RLock()
i = 0

def main():
	for i in range(100):
		myA = MyThreadA()
		myB = MyThreadB()
		myA.start()
		myB.start()


if __name__ == '__main__':
	main()