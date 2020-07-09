import socket
address = ('127.0.0.1', 31500)  # 服务端地址和端口
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    trigger = input('Input: ')
    if trigger:
        s.sendto(trigger.encode(), address)
        data, addr = s.recvfrom(1024)  # 返回数据和接入连接的（服务端）地址
        data = data.decode()
        print('[Recieved]', data)
        if trigger == '###':  # 自定义结束字符串
            break
    else:
        print("qing 输入内容")
s.close()
