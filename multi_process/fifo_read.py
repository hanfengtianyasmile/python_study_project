#encoding:utf-8
import os, time, random

p_Name = "./pipe1"

if (os.access(p_Name, os.F_OK) == False) :
    os.mkfifo(p_Name)

print("before open")
fp_r = os.open(p_Name, os.O_RDONLY)
print("open end")
while True:
    time.sleep(2)
    msg = os.read(fp_r, 100)
    if msg == "":
        break
    print(msg)
    if msg == "q":
        print("quit")
        break
os.close(fp_r)