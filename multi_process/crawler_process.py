#使用gevent编写爬虫，效率很高，遇到io即自动切换

from urllib import request
import gevent, time
from gevent import monkey

#把当前程序所有io操作单独做上标记
monkey.patch_all()


def get_url(url):
    print('GET %s' % url)
    res = request.urlopen(url)
    data = res.read()
    print('%d bytes received from %s' % (len(data), url))


urls = ['https://www.baidu.com','http://www.sina.com','https://www.sohu.com']

time_start = time.time()

for url in urls:
    get_url(url)

print('同步cost',time.time() - time_start)

async_time_start = time.time()

gevent.joinall([
    gevent.spawn(get_url,urls[0]), #启动协程
    gevent.spawn(get_url,urls[1]),
    gevent.spawn(get_url,urls[2]),
])

print('异步cost', time.time() - async_time_start)