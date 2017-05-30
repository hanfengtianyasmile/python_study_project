import hashlib
import socket, os, time

charset = 'utf-8'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 9999))
server.listen()


while True:
    conn, addr = server.accept()
    print('新的连接来了%s:%s', addr)

    while True:
        print('等待指令')
        data = conn.recv(1024).decode(charset)

        if data == 'exit':
            print('客户端断开')
            break
        cmd, filename = data.split(' ')
        print(filename)

        if os.path.isfile(filename):
            f = open(filename, 'rb')
            md5 = hashlib.md5()

            file_size = os.stat(filename).st_size
            conn.send(str(file_size).encode(charset))
            conn.recv(1024)

            for line in f:
                md5.update(line)
                conn.send(line)

            print('file md5', md5.hexdigest())
            f.close()

            conn.send(md5.hexdigest().encode(charset))
        print("over")









