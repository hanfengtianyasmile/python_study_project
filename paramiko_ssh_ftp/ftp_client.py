'''
使用 paramiko 实现ftp 上传、下载文件效果
使用socket编程也是可以达到该效果，不过paramiko功能更强大，可以连接远程服务器执行命令、上传下载文件
'''



import paramiko

#创建ssh对象

transport = paramiko.Transport(('192.168.1.103', 22))
transport.connect(username='root', password='123456')

sftp = paramiko.SFTPClient.from_transport(transport)


# 上传本地文件
local_file_path = ''
remote_file_path = ''

sftp.put(local_file_path, remote_file_path)

# 下载远程文件
sftp.get(remote_file_path, local_file_path)


sftp.close()