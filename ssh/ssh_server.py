#ssh服务端

import socket
import os
import time

charset = 'utf-8'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 9999))
server.listen(5)

while True:
    conn, addr = server.accept()
    print('有新的连接过来了%s %s' % addr)
    while True:
        print('等待新的指令')

        data = conn.recv(1024).decode(charset)

        if data == 'exit':
            print('客户端主动断开')
            break

        print('执行指令', data)

        #执行输入命令
        cmd_res = os.popen(data).read()

        #判断执行有无输出，并返回客户端

        if len(cmd_res) == 0:
            cmd_res = 'no output...'

        #先返回客户端要返回数据的大小，从而让客户端好接受全部数据

        conn.send(str(len(cmd_res.encode(charset))).encode(charset))

        time.sleep(0.5)

        conn.send(cmd_res.encode(charset))

        print('传送完成')


