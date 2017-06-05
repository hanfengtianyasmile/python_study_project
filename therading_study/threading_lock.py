#coding:utf-8

#加线程锁可以防止多线程在上下文切换时造成数据错误，保证数据无误，锁的目的是保证同一份数据不会被两个线程同时修改
#当然Python3已经对此优化，无需加锁

import threading, time


def run(n):
    global num
    time.sleep(0.2)
    #加锁
    lock.acquire()

    num += 1
    #释放锁
    lock.release()



num = 0

lock = threading.Lock()

start_time = time.time()

t_jobs = []

for i in range(1000):
    #调用线程
    t = threading.Thread(target=run, args=("t-%s" % i, ))

    t.start()
    t_jobs.append(t)



for t in t_jobs:
    t.join()

print('all,num', num)


