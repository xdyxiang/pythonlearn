import socket
address = ('127.0.0.1', 31500)  # 服务端地址和端口
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(address)  # 绑定服务端地址和端口
while True:
    data, addr = s.recvfrom(1024)  # 返回数据和接入连接的（客户端）地址
    data = data.decode()
    if not data:
        break
    print('[Received]', data)
    send = f"接受到{addr}的消息：{data}"
    s.sendto(send.encode(), addr)  # UDP 是无状态连接，所以每次连接都需要给出目的地址
s.close()
