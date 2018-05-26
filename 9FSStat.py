#! /usr/bin/env python3
import os
stat = os.statvfs(".")
print("total space: {0}".format((((int(stat.f_blocks) * int(stat.f_bsize)) >> 29) + 1) >> 1))
print("free space: {0}".format((((int(stat.f_bfree) * int(stat.f_bsize)) >> 29) + 1) >> 1))
print("free inodes: {0}".format(stat.f_ffree))
print("maximum filename length: {0}".format(stat.f_namemax))
