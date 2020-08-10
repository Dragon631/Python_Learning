# -*- coding: utf-8 -*-
"""
File Name:     19-socket-tcp-单进程非阻塞
"""
from socket import *

# 创建套接字对象
tclSerSock = socket(AF_INET, SOCK_STREAM)

# 设置socket选项，当socket关闭后，本地端用于该socket的端口号立刻就可以被重用
# 通常来说，只有经过系统定义一段时间后(2MSL)，才能被重用
tclSerSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

# 绑定socket，s.bind((host,port))
# 其中host为服务器ip，通常为空，也可以绑定到一个特定的ip地址, port为端口号
localaddr = ('192.168.100.65', 8080)
tclSerSock.bind(localaddr)

# 监听连接，该函数只有一个参数
# 其指明了在服务器实际处理连接的时候，允许有多少个等待的连接在队列中等待
tclSerSock.listen(5)
print("监听已准备好，等待新客户端连接的到来...")

# 设置服务端套接字为非阻塞模式
tclSerSock.setblocking(False)

# 定义一个列表保存客户端连接信息
clientsInfo = []
while True:
    try:
        newSockInfo = tclSerSock.accept()
    except Exception as result:
        pass
    else:
        print("来了一个新的客户端连接：%s" % str(newSockInfo[1]))
        newSockInfo[0].setblocking(False)
        clientsInfo.append(newSockInfo)

    removeClientInfo = []
    # 收取客户端数据
    for tcpCliSock, clientAddr in clientsInfo:
        try:
            recvData = tcpCliSock.recv(2014)
        except :
            pass
        else:
            if len(recvData) > 0:
                print("收到来自%s 的数据：%s" % (clientAddr, 
                    recvData.decode('gb2312')))
            else:
                tcpCliSock.close()
                removeClientInfo.append((tcpCliSock, clientAddr))
                print("客户端%s 连接已关闭！" % str(clientAddr))


    for deleteInfo in removeClientInfo:
        removeClientInfo.remove(deleteInfo)



