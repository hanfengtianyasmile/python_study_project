'''
使用 paramiko 连接服务端来执行ssh命令
通过私钥来登录服务器，而非账号密码,前提 ssh-copy-id user@host  将生成的公钥传送给服务器
'''



import paramiko

#创建ssh对象

private_key_path = ''

private_key = paramiko.RSAKey.from_private_key_file(private_key_path)

ssh = paramiko.SSHClient()

#允许连接不在Know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())


#连接主机
ssh.connect(hostname='192.168.1.1', port=22, username='root', pkey=private_key)

#执行命令

stdin, stdout, stderr = ssh.exec_command('ls')


#获取执行结果

result = stdout.read()

print(result.decode())

ssh.close()

