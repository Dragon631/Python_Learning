import threading

def test():
	lock = threading.RLock()
	lock.acquire()
	print("---1---")
	lock.acquire()
	print("---2---")
	lock.acquire()
	print("---3---")
	lock.release()
	lock.release()
	lock.release()

test()