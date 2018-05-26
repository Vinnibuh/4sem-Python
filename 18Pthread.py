#! /usr/bin/env python3
import threading
import _thread
from time import sleep
global a
a = 0
class Obj:
    def __init__(self, n):
        self.data = n
def thr_worker(obj):
    while (a != 1):
        obj.data +=1

x = Obj(0)
try:
    t = threading.Thread(target=thr_worker, args = (x,))
    t.start()
except:
    print("Errors in thread")

for i in range(10):
    sleep(1)
    print(x.data)
a = 1




        
