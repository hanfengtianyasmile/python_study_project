#当多个进程需要访问共享资源的时候，Lock可以用来避免访问的冲突。 比如多个进程共同写一个文件

import multiprocessing
import sys


def worker_with(lock, f):
    with lock:
        fs = open(f, "a+")
        fs.write('Lock acquired via with\n')
        fs.close()


def worker_no_with(lock, f):
    lock.acquire()
    try:
        fs = open(f, "a+")
        fs.write('Lock acquired directly\n')
        fs.close()
    finally:
        lock.release()


if __name__ == "__main__":
    f = "file.txt"

    lock = multiprocessing.Lock()
    #要讲锁传递给子进程，不然子进程无法获取到锁
    w = multiprocessing.Process(target=worker_with, args=(lock, f))
    nw = multiprocessing.Process(target=worker_no_with, args=(lock, f))

    w.start()
    nw.start()

    w.join()
    nw.join()