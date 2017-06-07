#在gevent中用到的主要模式是Greenlet, 它是以C扩展模块形式接入Python的轻量级协程  即自动切换线程
#可参考 gevent程序员指南[http://xlambda.com/gevent-tutorial/]
import gevent

def foo():
    print('aaa111')
    gevent.sleep(3)
    print('aaa222')

def bar():
    print('bbb111')
    gevent.sleep(2)
    print('bbb222')


def test():
    print('ccc111')
    gevent.sleep(1)
    print('ccc222')


gevent.joinall([
    gevent.spawn(foo),
    gevent.spawn(bar),
    gevent.spawn(test)
])

