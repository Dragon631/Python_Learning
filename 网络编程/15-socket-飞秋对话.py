# -*- coding: utf-8 -*-
# @Date_Time: 2019-06-19 16:54:30
# @File_Name: 12-socket-飞秋对话.py


from socket import *


def send_msg():
    # 1. 创建udp socket
    udp_socket_send = socket(AF_INET, SOCK_DGRAM)
    send_data = '1:100:Dragon:windows:32:Hello'
    # 1表示版本号，100标识包号，Dragon表示用户名，第二个windows表示主机名
    # 32表示发送消息，后面的表示要发送的消息内容
    send_data1 = '1_lbt80_0#32899#6045CB6240A4#0#0#0#4000#9:1561019633:a:DESKTOP-JC5CIA6:288:hellohello'
    udp_socket_send.sendto(send_data1.encode('utf-8'), ('192.168.100.65', 2425))
    udp_socket_send.close()

def main():
    send_msg()


if __name__ == '__main__':
    main()