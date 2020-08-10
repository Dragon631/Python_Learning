import queue

q = queue.Queue(4)
q.put(1)
# q.put(2)
# q.put(3)
# q.put(4, timeout=1)
# q.put(4, timeout=1)
# q.put(4, timeout=1)
print(q.get(timeout=1))
print(q.get(timeout=1))

