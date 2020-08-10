import multiprocessing
import os
def test(n):
	sum = 0
	print("子进程(%s)" % os.getpid)
	for i in range(1,n+1):
		sum += n
	return sum

def main():
	alist = [50,60,80]
	with multiprocessing.Pool(4) as pool:
		mp = pool.map(test, alist)
		for i in mp:
			print(i)


if __name__ == '__main__':
	main()
