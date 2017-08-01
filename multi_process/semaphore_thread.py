

import threading
import random
import time


class MyThread(threading.Thread):
    availableTables = ['A', 'B', 'C']

    def __init__(self, threadName, semaphore):
        self.interval = 1
        self.semaphore = semaphore
        threading.Thread.__init__(self, name=threadName)

    def run(self):
        # 获取信号量
        self.semaphore.acquire()
        print("entered;seated at table %s." % self.getName())
        time.sleep(1)

        self.semaphore.release()


mySemaphore = threading.Semaphore(3)


def Test():
    threads = []

    for i in range(1, 10):
        threads.append(MyThread("thread" + str(i), mySemaphore))

    for i in range(len(threads)):
        threads[i].start()


if __name__ == '__main__':
    Test()