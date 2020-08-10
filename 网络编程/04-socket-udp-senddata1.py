# -*- coding: utf-8 -*-
# @Date_Time: 2019-06-14 10:15:51
# @File_Name: 04-socket-udp-senddata1.py

from socket import *


def send_msg():
    # 1. 创建udp socket
    udp_socket_send = socket(AF_INET, SOCK_DGRAM)

    while True:
        # 1.1 输入要发送的数据
        send_data = input('请输入要发送的数据：')
        if send_data == 'exit':
            break

        # 2. 发送data
        udp_socket_send.sendto(send_data.encode('utf-8'), ('192.168.100.160', 8081))

    # 3. 关闭udp_socket
    udp_socket_send.close()


def main():
    send_msg()


if __name__ == '__main__':
    main()