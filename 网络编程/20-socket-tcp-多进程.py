# -*- coding: utf-8 -*-
# @Date_Time: 2019-06-21 16:09:33
# @File_Name: 20-socket-tcp-多进程.py


from socket import *
from multiprocessing import Process

# 定义子进程调用方法
def receiveData(newCliSock, newClientAddr):
    while True:
        recvData = newCliSock.recv(1024)
        if len(recvData) > 0:
            print("收到来自%s 的数据：%s" % (str(newClientAddr),
                recvData.decode('gb2312')))
        else:
            print("客户端已关闭连接...")
            break
    newCliSock.close()

def main():
    # 创建套接字对象
    tclSerSock = socket(AF_INET, SOCK_STREAM)

    # 设置socket选项，当socket关闭后，本地端用于该socket的端口号立刻就可以被重用
    # 通常来说，只有经过系统定义一段时间后(2MSL)，才能被重用
    tclSerSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    # 绑定socket，s.bind((host,port))
    # 其中host为服务器ip，通常为空，也可以绑定到一个特定的ip地址, port为端口号
    localaddr = ('', 8081)
    tclSerSock.bind(localaddr)

    # 监听连接，该函数只有一个参数
    # 其指明了在服务器实际处理连接的时候，允许有多少个等待的连接在队列中等待
    tclSerSock.listen(10)
    print("监听已启动...")

    try:
        while True:
            # print('主进程，等待新客户端的到来')
            newSock, newAddr = tclSerSock.accept()
            print("创建新客户端套接字处理数据：%s" % str(newAddr))
            p = Process(target=receiveData, args=(newSock, newAddr))
            p.start()

            newSock.close()
    finally:
        tclSerSock.close()

if __name__ == "__main__":
    main()









