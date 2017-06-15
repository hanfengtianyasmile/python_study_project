# python_study_project
Python学习项目

### ftp

socket编程，可以下载文件，并对文件做MD5验证

### ftp_object

socket编程，向服务端上传文件，并且服务端使用socketserver包来实现服务端与多线程

### socket_server

socketserver包的小例子


### ssh

socket编程，实现简单的ssh功能

### paramiko

paramiko模块，可以实现ssh、ftp功能

连接服务器可采用账号密码、秘钥公钥方式，可参考 [SSH原理与运用](http://www.ruanyifeng.com/blog/2011/12/ssh_remote_login.html) 、 [数字签名是什么？](http://www.ruanyifeng.com/blog/2011/08/what_is_a_digital_signature.html)

### Event

Event是Python多线程通信的最简单的机制之一.一个线程标识一个事件,其他线程一直处于等待状态。

### thread_queue

生产者、消费者模型，线程通过队列来通信


### gevent_server

使用gevent库 ，单线程开启协程也能来实现并发


### multi_process

包含多进程、进程通信、进程锁等实例

### XPath

对XPath的学习，实践了一个爬取百度贴吧回复的实例