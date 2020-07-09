import socket
import struct
import json,os

# 定义路径全局变量,这里为客户端下载文件到本地的保存路径
Download_dir = os.path.join(os.path.dirname(__file__), "filedir2")
# 建立
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接
phone.connect(('127.0.0.1', 8081))
while True:
    cmd = input('>>> ').strip()
    if not cmd:
        continue
    if cmd == 'quit':
        break
    # 给服务端发送命令
    phone.send(cmd.encode('utf-8'))
    # 接收服务端数据

    # 1.先收报头长度
    obj = phone.recv(4)
    header_size = struct.unpack('i', obj)[0]
    # 2.收报头
    '''
            header_dic = {
            'filename': filename,
            'file_size': os.path.getsize(filename)
        }
    '''
    header_bytes = phone.recv(header_size)
    # 3.从报头中解析出数据的真实信息（报头字典）
    header_json = header_bytes.decode('utf-8')
    header_dic = json.loads(header_json)
    # 4.解析命令
    total_size = header_dic['file_size']
    filename = header_dic['filename']

    # 4.接受真实数据
    with open('%s/%s' % (Download_dir, filename), 'wb') as f:
        recv_size = 0
        while recv_size < total_size:
            line = phone.recv(1024)
            f.write(line)
            recv_size += len(line)
            # print('总大小：%s     已下载：%s' % (total_size, recv_size))

# 关闭套接字
phone.close()
