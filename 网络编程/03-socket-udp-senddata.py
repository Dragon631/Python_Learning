import socket


def send_msg():
    # 1. 创建udp socket
    udp_socket_send = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

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