# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     chat_server
   Description :
   Author :       a
   date:          2019/4/19
-------------------------------------------------
"""
__author__ = 'a'

from socket import *

ip = '127.0.0.1'
port = 10055
addr = (ip, port)
buf = 1024
ss = socket(AF_INET, SOCK_STREAM)
ss.bind(addr)
ss.listen(5)

print("Waiting for connection...")
while True:

    conn, clnt_addr = ss.accept()
    print("Connected with ", clnt_addr)
    rc_data = conn.recv(buf).decode('utf-8')  # received data from client
    print("\033[31mClient_#%s\033[0m" % rc_data)
    ss_data = input("\033[33mServer_#\033[0m")
    if ss_data == 'q':
        break
    conn.send(ss_data.encode('utf-8'))
    conn.close()
ss.close()

"""
import socket
#创建服务端的socket对象socketserver
socketserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '10.36.135.90'
port = 9092
#绑定地址（包括ip地址会端口号）
socketserver.bind((host, port))
#设置监听
socketserver.listen(5)
#等待客户端的连接
#注意：accept()函数会返回一个元组
#元素1为客户端的socket对象，元素2为客户端的地址(ip地址，端口号)
clientsocket,addr = socketserver.accept()
 
#while循环是为了能让对话一直进行，直到客户端输入q
while True:
 
    #接收客户端的请求
    recvmsg = clientsocket.recv(1024)
    #把接收到的数据进行解码
    strData = recvmsg.decode("utf-8")
    #判断客户端是否发送q，是就退出此次对话
    if strData=='q':
        break
    print("收到:"+strData)
    msg = input("回复:")
    #对要发送的数据进行编码
    clientsocket.send(msg.encode("utf-8"))
 
socketserver.close()
"""



