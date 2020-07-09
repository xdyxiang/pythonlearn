
# socket的参数：
# 参数一：地址簇
# 　　socket.AF_INET IPv4（默认）
# 　　socket.AF_INET6 IPv6
# 　　socket.AF_UNIX 只能够用于单一的Unix系统进程间通信
# 参数二：类型
# 　　socket.SOCK_STREAM　　流式socket , for TCP （默认）
# 　　socket.SOCK_DGRAM　　 数据报式socket , for UDP
# 　　socket.SOCK_RAW 原始套接字，普通的套接字无法处理ICMP、IGMP等网络报文，而SOCK_RAW可以；其次，SOCK_RAW也可以处理特殊的IPv4报文；此外，利用原始套接字，可以通过IP_HDRINCL套接字选项由用户构造IP头。
# 　　socket.SOCK_RDM 是一种可靠的UDP形式，即保证交付数据报但不保证顺序。SOCK_RAM用来提供对原始协议的低级访问，在需要执行某些特殊操作时使用，如发送ICMP报文。SOCK_RAM通常仅限于高级用户或管理员运行的程序使用。
# 　　socket.SOCK_SEQPACKET 可靠的连续数据包服务

# 参数三：协议
# 　　0　　（默认）与特定的地址家族相关的协议,如果是 0 ，则系统就会根据地址格式和套接类别,自动选择一个合适的协议


import socket
address = ('127.0.0.1', 5005)  # 服务端地址和端口
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(address)  # 绑定服务端地址和端口
s.listen(5)
conn, addr = s.accept()  # 返回客户端地址和一个新的 socket 连接
print('[+] Connected with', addr)
while True:
    data = conn.recv(1024)  # buffersize 等于 1024
    data = data.decode()
    if not data:
        break
    print('[Received]', data)
    send = f"接收到消息：{data}"
    conn.sendall(send.encode())
conn.close()
s.close()