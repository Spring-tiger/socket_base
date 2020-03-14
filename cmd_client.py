# author:荒
# date:2020/3/14
# 发送远程命令，接收命令执行结果

import socket
from socket import *

# family type
# family 可选AF_INET6 ipv6    AF_UNIX:Unix不同进程间通信
# type可选SOCK_DGRAM

sk = socket(family=AF_INET, type=SOCK_STREAM)
address = ('127.0.0.1', 8000)  # 想连接哪个服务器，就写他的ip和端口
sk.connect(address)

while True:
    inp = bytes(input(">>>"), 'utf8')
    if str(inp, 'utf8') == 'exit':
        break
    sk.send(inp)

    data_len = int(str(sk.recv(1024), 'utf8'))  # 传大文件，分次接收
    print(data_len)
    data = bytes()
    while len(data) != data_len:
        data += sk.recv(1024)

    print(str(data, 'gbk'))
    # if not data:
    #     print('dddddddd')
    #     continue

print('not over')
# sk.close()
