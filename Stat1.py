#!/usr/bin/env python3
import os
fd = os.open("FirstTry.txt", os.O_RDWR, os.O_CREAT)
struct = os.fstat(fd)
print("Size of file: {}".format(struct.st_size))
print("File type: {}".format(struct.st_mode))
print("Owner ID: {}".format(struct.st_uid))
print("Time of last modification: {}".format(struct.st_mtime))

