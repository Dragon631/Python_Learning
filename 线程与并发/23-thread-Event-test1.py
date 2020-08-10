import threading
class Account:
    # 定义构造器
    def __init__(self, account_no, balance):
        # 封装账户编号、账户余额的两个成员变量
        self.account_no = account_no
        self._balance = balance
        self.lock = threading.Lock()
        self.event = threading.Event()
    # 因为账户余额不允许随便修改，所以只为self._balance提供getter方法
    def getBalance(self):
        return self._balance
    # 提供一个线程安全的draw()方法来完成取钱操作
    def draw(self, draw_amount):
        # 加锁
        self.lock.acquire()
        # 如果Event内部旗标为True，表明账户中已有人存钱进去
        # 执行取钱操作
        print(threading.current_thread().name
            + " 取钱:" +  str(draw_amount))
        self._balance -= draw_amount
        print("账户余额为：" + str(self._balance))
        self.lock.release()

    def deposit(self, deposit_amount):
        # 加锁
        self.lock.acquire()
        # 如果Event内部旗标为False，表明账户中还没有人存钱进去
        # 执行存款操作
        print(threading.current_thread().name\
            + " 存款:" +  str(deposit_amount))
        self._balance += deposit_amount
        print("账户余额为：" + str(self._balance))
        # 释放加锁
        self.lock.release()

def main():
    a = Account('001', 1000)
    threading.Thread(target=a.draw, args=(100,), name="甲").start()
    threading.Thread(target=a.draw, args=(100,), name="乙").start()
    threading.Thread(target=a.draw, args=(100,), name="丙").start()
    threading.Thread(target=a.deposit, args=(100,), name="甲").start()
    threading.Thread(target=a.deposit, args=(100,), name="乙").start()
    threading.Thread(target=a.deposit, args=(100,), name="丙").start()
    threading.Thread(target=a.deposit, args=(100,), name="丙").start()
    threading.Thread(target=a.deposit, args=(100,), name="丙").start()
    threading.Thread(target=a.deposit, args=(100,), name="丙").start()
    

if __name__ == '__main__':
    main()