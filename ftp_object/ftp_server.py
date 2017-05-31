#上传文件

import socketserver, json, os


charset = 'utf-8'


class MyTcpHandler(socketserver.BaseRequestHandler):

    def put(self, *args):
        cmd_dic = args[0]

        filename = cmd_dic['filename']
        file_size = cmd_dic['size']

        if os.path.isfile(filename):
            f = open('new'+filename, 'wb')
        else:
            f = open(filename, 'wb')

        self.request.send(b"200 ok")
        received_size = 0

        while received_size < file_size:
            data = self.request.recv(1024)
            f.write(data)
            received_size += len(data)
        else:
            print('file %s upload' % filename)

    def handle(self):
        while True:
            self.data = self.request.recv(1024).strip()
            print("{} write".format(self.client_address[0]))
            print(self.data)
            cmd_dic = json.loads(self.data.decode('utf-8'))
            print(cmd_dic)
            action = cmd_dic["action"]

            if hasattr(self, action):
                func = getattr(self, action)
                func(cmd_dic)


if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 9999), MyTcpHandler)
    server.serve_forever()








