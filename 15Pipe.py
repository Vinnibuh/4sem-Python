#! /usr/bin/env python3
import os
import fcntl as f
try:
    ppe = os.pipe()
except:
    print("Pepe error")
try:
    f.fcntl(ppe[1], f.F_SETFL, f.fcntl(ppe[0], f.F_GETFL) | os.O_NONBLOCK)
except OSError:
    print("fcntl error")
size = 1
summ = 0
n = 1000
buf = bytearray(n)
while size!= 0:
    try:    
        size = os.write(ppe[1], buf[:n])
        summ += size
    except:
        n = n // 2
print(summ)
