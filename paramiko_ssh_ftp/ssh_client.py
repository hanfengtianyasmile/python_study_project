'''
使用 paramiko 连接服务端来执行ssh命令
使用socket编程也是可以达到该效果，不过paramiko功能更强大，可以连接远程服务器执行命令、上传下载文件
'''



import paramiko

#创建ssh对象

ssh = paramiko.SSHClient()

#连接主机
ssh.connect(hostname='192.168.1.1', port=22, username='root', password='123456')

#执行命令

stdin, stdout, stderr = ssh.exec_command('ls')


#获取执行结果

result = stdout.read()

print(result.decode())


ssh.close()