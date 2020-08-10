import queue
# FIFO
fifo = queue.Queue()
for i in range(5):
	fifo.put(i)
	print("FIFO: %d 入列..." % i)
print("-"*15)
for i in range(fifo.qsize()):
	print("FIFO: %d 出列" % fifo.get())

print("#"*15)
# FILO
lifo = queue.LifoQueue()
for i in range(5):
	lifo.put(i)
	print("LIFO: %d 入列..." % i)
print("-"*15)
for i in range(lifo.qsize()):
	print("LIFO: %d 出列..." % lifo.get())

print("#"*15)
# FILO
pq = queue.PriorityQueue()
for i in range(5 // 2):
	pq.put(i)
	print("pq: %d 入列..." % i)
for i in range(7 // 3):
	pq.put(i)
	print("pq: %d 入列..." % i)
print("-"*15)
for i in range(pq.qsize()):
	print("pq: %d 出列..." % pq.get())
print(dir(pq))
print(help(pq))