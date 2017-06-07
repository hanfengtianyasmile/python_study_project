#进程池 Pool可以提供指定数量的进程供用户调用，当有新的请求提交到pool中时，如果池还没有满，那么就会创建一个新的进程用来执行该请求；但如果池中的进程数已经达到规定最大值，那么该请求就会等待，直到池中有进程结束，空闲的进程才会去处理新的任务
#coding: utf-8
import multiprocessing
import time,os

def func(msg):
    print("msg:", msg)
    print('get pid',os.getpid())
    time.sleep(3)
    print("end")

if __name__ == "__main__":
    pool = multiprocessing.Pool(processes = 3)
    result = []
    for i in range(6):
        msg = "hello %d" %(i)
        result.append(pool.apply_async(func, (msg, )))   #进程池在旧进程的任务执行完毕后，不会创建新的子进程，是刚刚空闲出来的进程去执行新的任务，进程池中的各进程pid是不变的

    print("Mark~ Mark~ Mark~~~~~~~~~~~~~~~~~~~~~~")
    pool.close()
    pool.join()   #调用join之前，先调用close函数，否则会出错。执行完close后不会有新的进程加入到pool,join函数等待所有子进程结束
    for res in result:
        print(res.get())
    print("Sub-process(es) done.")