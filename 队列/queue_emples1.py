import threading
import queue
import time


class worker(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
        self.thread_stop = False

    def run(self):
        while not self.thread_stop:
            print("thread%d %s: waiting for tast" % (self.ident, self.name))
            try:
                # task = q.get()  # 接收消息
                task = q.get(block=True, timeout=1)  # 接收消息
            except queue.Empty:
                print("Nothing to do! I will go home!")
                self.thread_stop = True
                break
            print("tasking: %s ,task No:%d" % (task[0], task[1]))
            print("I am working")
            time.sleep(1)
            print("work finished!")
            q.task_done()                           # 完成一个任务
            res = q.qsize()                         # 判断消息队列大小(队列中还有几个任务)
            if res > 0:
                print("fuck! Still %d tasks to do" % (res))

    def stop(self):
        self.thread_stop = True


if __name__ == "__main__":
    q = queue.Queue(3)                                    # 创建队列（大小为3）
    worker = worker(q)                                    # 将队列加入类中
    worker.start()                                        # 启动类
    q.put(["produce cup!", 1], block=True, timeout=None)  # 向队列中添加元素，产生任务消息
    q.put(["produce desk!", 2], block=True, timeout=None)
    q.put(["produce apple!", 3], block=True, timeout=None)
    q.put(["produce banana!", 4], block=True, timeout=None)
    q.put(["produce bag!", 5], block=True, timeout=None)
    print("***************leader:wait for finish!")
    q.join()                                             # 等待所有任务完成
    print("***************leader:all task finished!")