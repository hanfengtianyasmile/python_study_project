import socketserver, json, os


charset = 'utf-8'


class MyTcpHandler(socketserver.BaseRequestHandler):

    def handle(self):
        while True:

            self.data = self.request.recv(1024).strip()
            print("{} write".format(self.client_address[0]))
            print(self.data)
            cmd_dic = json.loads(self.data.decode('utf-8'))
            action = cmd_dic["action"]

            if hasattr(self, action):
                func = getattr(self,action)
                func(cmd_dic)













