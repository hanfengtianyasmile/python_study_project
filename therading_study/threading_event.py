#Event是Python多线程通信的最简单的机制之一.一个线程标识一个事件,其他线程一直处于等待状态。

import time
import threading


event = threading.Event()

def lighter():
    count = 0
    event.set() #先设置绿灯
    while True:
        if count >5 and count < 10: #改成红灯
            event.clear() #把标志位清了
            print("\033[41;1mred light is on....\033[0m")
        elif count >10:
            event.set() #变绿灯
            count = 0
        else:
            print("\033[22;1mgreen light is on....\033[0m")
        time.sleep(1)
        count +=1

def car(name):
    while True:
        if event.is_set(): #代表绿灯
            print("[%s] running..."% name )
            time.sleep(1)
        else:
            print("[%s] sees red light , waiting...." %name)
            event.wait()
            print("\033[34;1m[%s] green light is on, start going...\033[0m" %name)


light = threading.Thread(target=lighter,)
light.start()

car1 = threading.Thread(target=car,args=("Tesla",))
car1.start()

