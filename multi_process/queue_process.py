#通过进程队列来实现进程通信

from multiprocessing import Process, Queue
import threading, time

def f(q):
    time.sleep(3)
    q.put('456')
    pass

if __name__ == '__main__':
    q = Queue()
    q.put('123')

    print("data",q.get())
    p = Process(target=f, args=(q,))
    p.start()
    p.join()
    print('get second data')
    print("data",q.get())
    print("data", q.get())

