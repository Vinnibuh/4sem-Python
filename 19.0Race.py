#! /usr/bin/env python3
import threading
import os
from sys import getsizeof
import struct
from time import sleep

global a

def worker():
    try:
        fd = os.open("Example.txt", os.O_RDWR)
    except:
        print("error in open")
    n = os.read(fd, 4)
    try:
        x, = struct.unpack('i', n)
    except:
        print("error in read or unpack")
    x += 1
    n = struct.pack('i', x)
    rd_size = os.write(fd, n)
    os.close(fd)
    sleep(1)

fd = os.open("Example.txt", os.O_RDWR | os.O_CREAT | os.O_TRUNC)
n = struct.pack('i', 0)
os.write(fd, n)
t = []
for i in range(10):
    try:
        t.append(threading.Thread(target=worker))
        t[i].start()
    except:
        print("error in starting threads")
for i in range(10):
    t[i].join()
sleep(1)
n = os.read(fd, 4)
x, = struct.unpack('i', n)
print(x)
os.close(fd)
sleep(1)





