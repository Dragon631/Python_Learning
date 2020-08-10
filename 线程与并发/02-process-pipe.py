from multiprocessing import Pipe, Process, current_process 

# 定义pipe发送端
def send_client(conn):
	data = "Hello World!"
	print("【发送进程-%d】 发送数据： %s" % (current_process().pid, data))
	for i in data:
		conn.send(i)	# 使用conn发送数据

# 定义pipe接收端
def recv_client(conn):
	while True:
		result = conn.recv() # 使用conn接收数据
		print("【接收进程-%d】 接收数据： %s" % (current_process().pid, result))
		if not conn.poll():
			break

def main():
	# 创建Pipe，该函数返回两个PipeConnection对象
	send_conn, recv_conn = Pipe()
	# 创建子进程
	ps = Process(target=send_client, args=(send_conn, ))
	pr = Process(target=recv_client, args=(recv_conn, ))
	ps.start()	# 启动子进程
	pr.start()  # 启动子进程
	ps.join()
	pr.join()
	ps.close()
	pr.close()

if __name__ == '__main__':
	main()

