# author:荒
# date:2020/3/13

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

    data = sk.recv(1024)
    print(str(data, 'utf8'))

print('not over')
# sk.close()
