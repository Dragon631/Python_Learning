class Foo(object):
	"""docstring for Foo"""
	def __init__(self, num):
		super(Foo, self).__init__()
		self.num = num
		self.__num = 200

	def getNum(self):
		print("------getNum------")
		print("__num = %d" % self.__num)

	def setNum(self, num):
		print("------setNum to %d------" % num)
		self.__num = num

	temp = property(getNum, setNum)

if __name__ == '__main__':
	f = Foo(100)
	temp = 123
	f.getNum()
	f.setNum(123)
	f.getNum()