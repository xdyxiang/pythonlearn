import socket
import json
import struct
import os

# 定义路径全局变量,这里为服务端提供文件的路径
share_dir = os.path.join(os.path.dirname(__file__), "filedir")

# 建立
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# 绑定
phone.bind(('127.0.0.1', 8081))

# 监听
phone.listen(5)

# 通信循环
while True:
    # 接收客户端连接请求
    conn, client_addr = phone.accept()
    while True:
        # 接收客户端数据/命令
        res = conn.recv(1024)
        if not res:
            continue
        # 解析命令 'get 1.mp4'
        cmds = res.decode('utf-8').split()  # ['get','1.mp4']
        print(type(cmds))
        print(cmds)

        filename = cmds[1]  # '1.mp4'
        # 以读的方式打开文件，提取文件内容发送给客户端
        # 1.制作固定长度的报头
        header_dic = {
            'filename': filename,
            'file_size': os.path.getsize('{}/{}'.format(share_dir, filename))
        }
        # 序列化报头
        header_json = json.dumps(header_dic)  # 序列化为byte字节流类型
        header_bytes = header_json.encode('utf-8')  # 编码为utf-8（Mac系统）
        # 2.先发送报头的长度
        # 2.1 将byte类型的长度打包成4位int
        conn.send(struct.pack('i', len(header_bytes)))
        # 2.2 再发报头
        conn.send(header_bytes)
        # 2.3 再发真实数据
        with open('{}/{}'.format(share_dir, filename), 'rb') as f:
            for line in f:
                conn.send(line)
    # 结束连接
    conn.close()

# 关闭套接字
phone.close()
