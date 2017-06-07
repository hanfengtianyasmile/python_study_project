#多进程使用，获取进程号
__author__ = "Alex Li"

from multiprocessing import Process
import os


def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())



def f(name):
    info('called from child process function ')
    print('hello', name)

if __name__ == '__main__':
    info('main process line')
    p = Process(target=f, args=('bob',))
    p.start()