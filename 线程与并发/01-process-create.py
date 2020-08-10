import multiprocessing
from time import sleep
# 定义写数据进程函数
def write(q):
	str = "Hello Wrold"
	print("【写数据进程-%d】 将数据放入队列中..." % multiprocessing.current_process().pid)
	for i in str:
		q.put(i)

# 定义读数据进程函数
def read(q):
	print("【读数据进程-%d】 从队列中取出数据..." % multiprocessing.current_process().pid)
	while not q.empty():
		print(q.get_nowait())
# 定义main函数
def main():
	# 主进程开始
	print("【主进程-%d】 开始执行..." % multiprocessing.current_process().pid)
	# 创建进程通信的Queue
	q = multiprocessing.Queue()

	# 创建子进程
	pw = multiprocessing.Process(target=write, args=(q, ))
	pr = multiprocessing.Process(target=read, args=(q, ))

	pw.start()       # 启动子进程
	pr.start()
	pr.join()		 # 阻塞到数据读取完成
	print("---程序处理完毕！---")

if __name__ == '__main__':
	main()

