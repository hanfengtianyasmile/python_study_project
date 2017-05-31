from socketserver import BaseRequestHandler, TCPServer, ThreadingTCPServer


class requestHandler(BaseRequestHandler):
    def handle(self):
        print('连接来了', self.client_address)
        while True:

            request_data = self.request.recv(1024)

            if not request_data:
                break
            self.request.send(request_data)

if __name__ == '__main__':
    '''
    单线程
    server = TCPServer(('127.0.0.1',9999), requestHandler)
    server.serve_forever()
    备注
    '''
    # 多线程
    server = ThreadingTCPServer(('127.0.0.1', 9999), requestHandler)
    server.serve_forever()

    # 备注：直接使用 socket 库来实现服务器也并不是很难，比如ssh小项目里,多线程也是直接再起一个线程即可







