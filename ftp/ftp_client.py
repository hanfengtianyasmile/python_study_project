import hashlib
import socket, os, time

charset = 'utf-8'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 9999))


while True:
    cmd = input('>>>:').strip()
    if len(cmd) == 0:
        continue

    if cmd.startswith("get"):
        client.send(cmd.encode(charset))
        file_total_size = int(client.recv(1024).decode(charset))
        client.send(b'read send file')
        received_size = 0
        filename = cmd.split()[1]

        f = open(filename+'.new', 'wb')
        md5 = hashlib.md5()

        while received_size < file_total_size:
            # 防止粘包
            if file_total_size - received_size >= 1024:
                size = 1024
            else:
                size = file_total_size - received_size
            data = client.recv(size)
            received_size += len(data)
            md5.update(data)
            f.write(data)

        new_file_md5 = md5.hexdigest()

        print('receive file info', received_size, file_total_size)

        f.close()

        server_file_md5 = client.recv(1024)

        print('client file md5', new_file_md5)
        print('server file md5', server_file_md5.decode(charset))



