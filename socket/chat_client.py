# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     chat_client
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
sc = socket(AF_INET, SOCK_STREAM)
sc.connect(addr)

while True:
    sc_data = input("Client_#")
    if sc_data == 'q':
        break
    sc.send(sc_data.encode('utf-8'))
    rc_data = sc.recv(buf).decode('utf-8')  # received data from server
    print("\033[32mServer_#%s\033[0m" % rc_data)
sc.close()

"""
import socket
#创建一个客户端的socket对象
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
#设置服务端的ip地址
host = "10.36.135.90"
#设置端口
port = 9092
#连接服务端
client.connect((host, port))
 
#while循环是为了保证能持续进行对话
while True:
    #输入发送的消息
    sendmsg = input("请输入:")
    #如果客户端输入的是q，则停止对话并且退出程序
    if sendmsg=='q':
        break
 
    sendmsg = sendmsg
    #发送数据，以二进制的形式发送数据，所以需要进行编码
    client.send(sendmsg.encode("utf-8"))
    msg = client.recv(1024)
    #接收服务端返回的数据，需要解码
    print(msg.decode("utf-8"))
#关闭客户端
client.close()
"""
