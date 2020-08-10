import threading
"""
需求：
1、一次只能允许一个人存款
2、一次只能允许一个人取款
3、当有人存款时，不能取款
4、当有人取款时，不能存款
"""
# ATM机
class ATM(object):
	# 初始化实例
	def __init__(self, account_no, balance):
		self.account_no = account_no
		self.__balance = balance
		self.lock = threading.RLock()
		self.event = threading.Event()

	# 获取余额
	def getBalance(self):
		return self.__balance

	# 存款
	def deposit(self, money):
		# 获取存款锁，进行存款		
		self.lock.acquire()
		# event标记True表示无人取款，可以存款
		if self.event.is_set():
			self.__balance += money
			print("%s 存款: %d 元，余额: %d " % (threading.current_thread().name, money, self.__balance))	
			# 存款完成，清楚event标记，并释放锁，使其他线程可以取款
			self.event.clear()
			self.lock.release()
			# 阻塞当前线程
			# self.event.wait()	
		else:
			self.lock.release()
			self.event.wait()
		# self.event.wait()
	# 取款
	def draw(self, money):
		# 获的取款锁，进行取款
		self.lock.acquire()
		# event标记False表示无人存款，可以取款
		if not self.event.is_set() and money <= self.__balance:
			self.__balance -= money
			print("%s 取款: %d 元，余额: %d " % (threading.current_thread().name, money, self.__balance))	
			# 取款完成，设置event标记，并释放锁，使其他线程可以存款			
			self.event.set()
			self.lock.release()
			# 阻塞当前线程
			self.event.wait() 
		else:
			self.lock.release()
			# 阻塞当前线程
			self.event.wait()

def main():
	a = ATM('001', 1000)
	threading.Thread(target=a.draw, args=(100,), name="甲").start()
	threading.Thread(target=a.draw, args=(100,), name="乙").start()
	threading.Thread(target=a.draw, args=(100,), name="丙").start()
	threading.Thread(target=a.deposit, args=(100,), name="甲").start()
	threading.Thread(target=a.deposit, args=(100,), name="乙").start()
	threading.Thread(target=a.deposit, args=(100,), name="丙").start()

if __name__ == '__main__':
	main()