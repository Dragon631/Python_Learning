from concurrent.futures import ThreadPoolExecutor

import threading
import time


def action(max):
	# time.sleep(1)
	print("%s start ... " % threading.currentThread().name)
	sum = 0	
	for i in range(max):
		sum += i
	return sum
	# print(sum)
def get_result(future):
	return future.result()

def customer():
	r = ''
	while True:
		n = yield r
		if not n:
			return
		print("cumstomer: cum---%d---" %n)
		r = '200 OK'

def productor(c):
	c.send(None)
	n = 0
	while n < 5:
		n += 1	
		print("productor: pro---%d---" % n)
		ret = c.send(n)
		print("product result: %s" % ret)
	# c.close()


def main():
	# tpool = ThreadPoolExecutor(4)
	# start_time = time.time()
	# future1 = tpool.submit(action,100000000)
	# future2 = tpool.submit(action,100000000)
	# future3 = tpool.submit(action,100000000)
	# future4 = tpool.submit(action,100000000)
	# future1.add_done_callback(get_result)
	# future2.add_done_callback(get_result)
	# future3.add_done_callback(get_result)
	# future4.add_done_callback(get_result)
	# print(future1.done())
	# print(future2.result())
	# print(future2.done())
	# print(future3.result())
	# print(future3.done())
	# print(future4.result())
	# print(future4.done())
	# tpool.shutdown()

	# t1 = threading.Thread(target=action,args=(100000000,))
	# t1.start()	
	# t2 = threading.Thread(target=action,args=(100000000,))
	# t2.start()
	# t3 = threading.Thread(target=action,args=(100000000,))
	# t3.start()	
	# t4 = threading.Thread(target=action,args=(100000000,))
	# t4.start()
	# t1.join()
	# t2.join()
	# t3.join()
	# t4.join()
	
	# end_time = time.time()
	# elapse = end_time - start_time
	# print(elapse)
	s=("C语言中文网是中国领先的C语言程序设计专业网站，\n"
	"提供C语言入门经典教程、C语言编译器、C语言函数手册等。")

	# print(s)

	c = customer()
	productor(c)


if __name__ == "__main__":
	main()






