import os,signal
from time import sleep


def onsignal_term(a,b):
    print('收到term信号')


def onsignal_usr1(a,b):
    print('收到user1信号')


signal.signal(signal.SIGTERM,onsignal_term)

signal.signal(signal.SIGUSR1,onsignal_usr1)

while True:
    print('我的进程id是',os.getpid())
    sleep(10)


