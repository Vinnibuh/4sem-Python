#! /usr/bin/env python3
import os
from threading import Timer
def Stats():
    print("Current Process ID = {}".format(os.getpid()))
    print("Current Process Parent ID = {}".format(os.getppid()))
    print("Current Process Session ID = {}".format(os.getsid(os.getpid())))
    print("Current Process Group ID = {}".format(os.getpgid(os.getpid())))

Stats()
try:
    ch_id = os.fork()
except:
    print("fork Error")
if ch_id == 0:
    t = Timer(3, Stats())
    t.start()
    print("Child process info:")
    pass
else:
    print("Parent process info:")
    Stats()
    os.wait()
    print("Once again:")
    Stats()



