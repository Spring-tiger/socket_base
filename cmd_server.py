# author:荒
# date:2020/3/14

import socket
from socket import *

import subprocess


# family type
# family 可选AF_INET6 ipv6    AF_UNIX:Unix不同进程间通信
# type可选SOCK_DGRAM
sersk = socket(family=AF_INET, type=SOCK_STREAM)
address = ('127.0.0.1', 8000)
sersk.bind(address)
sersk.listen(3)   # 3是最大等待数

while True:
    conn, addr = sersk.accept()
    print('new connect with: ')
    print(addr)
    while True:
        try:  # 避免客户端硬关闭，recv异常停止
            data = conn.recv(1024)
        except Exception as e:
            print(e)
            break

        if not data:  # 当前连接的客户端关闭了，若是他没发数据，则recv一直阻塞，不会返回
            conn.close()  # 我不跟你聊了
            break
        print(str(data, 'utf8'))
        # 执行接收的命令
        data = str(data, 'utf8')
        obj = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        cmd_res = obj.stdout.read()  # 返回执行的结果,bytes格式,gbk编码
        cmd_err = obj.stderr.read()
        print(str(cmd_err, 'gbk'))
        res_len = bytes(str(len(cmd_res)), 'utf8')  # int->str->bytes
        conn.send(res_len)
        # time.sleep(1)
        # 或者加一个recv（）  client加一个send
        conn.sendall(cmd_res)  # 可能出现粘包现象

sersk.close()    # 我谁都不想聊了
