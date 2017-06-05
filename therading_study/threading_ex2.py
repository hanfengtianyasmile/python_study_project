#线程简单使用
#守护线程，如果主线程结束，守护线程随之结束

import threading, time


def run(n):
    print("task", n)
    time.sleep(2)
    print("task done", n)


start_time = time.time()

t_jobs = []

for i in range(50):
    #调用线程
    t = threading.Thread(target=run, args=("t-%s" % i, ))
    #设置为守护线程
    t.setDaemon(True)
    t.start()
    t_jobs.append(t)

print('所有线程执行完毕，用时', time.time()-start_time)


