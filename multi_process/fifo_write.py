#encoding:utf-8
import os

p_Name = "./pipe1"

if os.access(p_Name, os.F_OK) == False:
    os.mkfifo(p_Name)
fd_w = os.open(p_Name, os.O_WRONLY)

while True:
    msg = input("w---->>")
    os.write(fd_w, msg.encode('utf-8'))
    if msg == "q":
        break
os.close(fd_w)