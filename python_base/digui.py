  # 遍历一个盘符下的所有文件（包括子文件夹、文件）

import os

def getFile(path):
    try:
        filelist = os.listdir(path)  # 得到该文件夹下的所有文件
        for file in filelist:
            file = os.path.join(path, file)  # 将文件名和路径结合起来
            if os.path.isdir(file):
                getFile(file)  # 在这里如果判断一个文件是文件夹，那么就会再次调用自己
            else:
                print(file)
    except:
        print('出错，跳过')

getFile(r'E:/')
