#ssh客户端


import socket


charset = 'utf-8'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('127.0.0.1', 9999))


while True:
    cmd = input(">>>:").strip()
    if len(cmd) == 0: continue
    client.send(cmd.encode(charset))
    cmd_res_size = client.recv(1024).decode(charset)

    if len(cmd_res_size) == 0:
        print('断开与服务端的连接')
        break

    print('命令结果大小', cmd_res_size)

    receive_size_sum = 0
    receive_data = b''

    while receive_size_sum < int(cmd_res_size):
        data = client.recv(1024)
        receive_size_sum += len(data)
        receive_data += data
    else:
        print('接受服务端返回数据', receive_data.decode(charset))


