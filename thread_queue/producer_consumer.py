#队列使用,生产者、消费者模型(线程使用)

import threading, time
import queue


q = queue.Queue(maxsize=10)


def producer(name):
    count = 1
    while True:
        q.put('生产%s' % count)
        print('%s 生产了 %d' % (name, count))
        count += 1
        time.sleep(0.1)


def consumer(name):
    while True:
        print('%s 取到了 %s' % (name, q.get()))
        time.sleep(1)


p = threading.Thread(target=producer, args=('hanfeng',))
c1 = threading.Thread(target=consumer, args=('xiao1',))
c2 = threading.Thread(target=consumer, args=('xiao2',))

p.start()
c1.start()
c2.start()