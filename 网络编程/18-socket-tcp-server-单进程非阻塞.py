# -*- coding: utf-8 -*-
# @Date_Time: 2019-06-21 10:21:10
# @File_Name: 18-socket-tcp-server-单进程非阻塞.py

from socket import *

# 1.创建套接字
tcpSocket = socket(AF_INET, SOCK_STREAM)
tcpSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

# 2.绑定ip-端口
ip_port = ('192.168.100.65', 8081)
tcpSocket.bind(ip_port)


# 3.监听端口，使套接字变为可以被动连接
tcpSocket.listen(5)
print("阻塞解除1：已准备好被动连接监听，等待客户端连接的到来...")

# 将套接字设置为非阻塞
tcpSocket.setblocking(False)

# 存放客户端连接信息
clientList = []

while True:
    try:
        # 4.accpet() 使套接字等待tcp客户端连接的到来
        clientInfo = tcpSocket.accept()
    except Exception as result:
        pass
    else:
        print("来了一个新的客户端连接：%s" % str(clientInfo))
        # 设置为非阻塞监听
        clientInfo[0].setblocking(False)
        clientList.append(clientInfo)

    # 5. 接收tcp数据
    for newSocket, clientAddr in clientList:
        try:
            recvData = newSocket.recv(1024)
        except:
            pass
        else:
            if len(recvData) > 0:
                print("收到来自%s 的信息：%s" % (clientAddr,
                    recvData.decode('gb2312')))
            else:
                newSocket.close()
                clientList.remove((newSocket, clientAddr))
                print("客户端%s连接已关闭..." % str(clientAddr))