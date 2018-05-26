#!/usr/bin/env python3
import os
from sys import getsizeof
example = "Something strange\n"
sz = getsizeof(example)
example = example.encode()
fd = os.open("FirstTry.txt", os.O_WRONLY | os.O_TRUNC | os.O_CREAT)
wr_flag = os.write(fd, example)
os.close(fd)
print("{0} vs {1}".format(sz, wr_flag))
