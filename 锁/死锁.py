import threading
import time

class MyThreadA(threading.Thread):
	def run(self):
		if mutexA.acquire():
			print("[%s]---A1---" % threading.current_thread().name)
			time.sleep(0.05)
			if mutexB.acquire():
				print("[%s]---A2---" % threading.current_thread().name)
			mutexA.release()

class MyThreadB(threading.Thread):
	def run(self):
		if mutexB.acquire():
			print("[%s]---B1---" % threading.current_thread().name)
			time.sleep(0.05)
			if mutexA.acquire():
				print("[%s]---B2---" % threading.current_thread().name)
			mutexB.release()

mutexA = threading.Lock()
mutexB = threading.Lock()
def main():
	myA = MyThreadA()
	myB = MyThreadB()

	myA.start()
	myB.start()


if __name__ == '__main__':
	main()