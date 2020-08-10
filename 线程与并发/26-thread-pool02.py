# coding=utf-8

import threading
import time
from concurrent.futures import ThreadPoolExecutor

pool = ThreadPoolExecutor(3)

def sub(max):
	r = 0
	print("线程: %s" % threading.current_thread().name)
	for i in range(max):
		r += i
	return r

future1 = pool.submit(sub, 1000000)
future2 = pool.submit(sub, 2000000)
future3 = pool.submit(sub, 4000000)
future4 = pool.submit(sub, 5000000)

time.sleep(2)
print(future1.done())
print(future2.done())
print(future3.done())
print(future4.done())

print(future1.result())
print(future2.result())
print(future3.result())
print(future4.result())


pool.shutdown()

