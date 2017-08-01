#多进程 管道 通信
from multiprocessing import Process, Pipe
import time

def chind(conn):
    conn.send('111')
    conn.send('222')
    print('from parent data', conn.recv())
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=chind, args=(child_conn, ))
    p.start()
    print(parent_conn.recv())
    print(parent_conn.recv())
    time.sleep(5)
    parent_conn.send('333')
    p.join()
