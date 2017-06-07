#已经知道如何使用yield关键字来实现协程，不过这个看上去非常不直观。可以学习一个非常好用的框架greenlet，很多知名的网络并发框架如eventlet，gevent都是基于它实现的。
#参考文章 用greenlet实现Python中的并发[http://www.bjhee.com/greenlet.html]

from greenlet import greenlet

def test1():
    print(12)
    gr2.switch()
    print(34)


def test2():
    print(56)
    gr1.switch()
    print(78)


gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr1.switch()
