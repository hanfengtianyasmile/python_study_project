#线程简单使用

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
    t.start()
    t_jobs.append(t)
#
# for t in t_jobs:
#     t.join()

print('所有线程执行完毕，用时', time.time()-start_time)


