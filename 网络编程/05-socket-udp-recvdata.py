# -*- coding: utf-8 -*-
# @Date_Time: 2019-06-14 10:29:44
# @File_Name: 05-socket-udp-recvdata.py

from socket import * 


def recv_msg():
    # 1. 创建套接字
    udp_socket_recv = socket(AF_INET, SOCK_DGRAM)

    # 2. bind ip和port
    ip_port = ('', 6666)
    udp_socket_recv.bind(ip_port)

    while True:
        # 3. 接收msg，recvfrom()返回的是一个元组，[0]是msg, [1]是一个元组的地址(ip, port)
        # 并且接收到的msg=tuple[0]是一个bytes类型，打印出来时是要decode的.
        msg, addr = udp_socket_recv.recvfrom(1024)
        # 4. 打印接收的msg，以 f' 开头，包含的{}表达式在程序运行时会被表达式的值代替
        print(f'收到来自{str(addr)}的信息:{msg.decode("utf-8")}')

    # 5. 关闭套接字
    udp_socket_recv.close()


def main():
    recv_msg()


if __name__ == '__main__':
    main()