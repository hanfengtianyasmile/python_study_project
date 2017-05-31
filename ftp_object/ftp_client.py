#用面向对象的方式写上传文件

import socket, json, os


charset = 'utf-8'

class FtpClient(object):
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, ip, port):
        self.client.connect((ip, port))

    def interactive(self):
        while True:
            cmd = input('>>').strip()
            if len(cmd) == 0: continue
            cmd_str = cmd.split()[0]
            if hasattr(self, "cmd_%s" % cmd_str):
                func = getattr(self, "cmd_%s" % cmd_str)
                func(cmd)

    def cmd_put(self, *args):
        cmd_split = args[0].split()
        if len(cmd_split) > 1:
            filename = cmd_split[1]
            if os.path.isfile(filename):
                filesize = os.stat(filename).st_size
                msg_dict = {
                    "action": "put",
                    "filename": filename,
                    "size": filesize,
                    "overridden": True
                }

                print('send data', json.dumps(msg_dict).encode(charset))
                self.client.send(json.dumps(msg_dict).encode(charset))
                #防止粘包，等待服务器确认
                server_response = self.client.recv(1024)
                f = open(filename,"rb")

                for line in f:
                    self.client.send(line)
                else:
                    print("file upload success")
                    f.close()
            else:
                print(filename, 'is not exist')


ftp = FtpClient()
ftp.connect('127.0.0.1', 9999)
ftp.interactive()


