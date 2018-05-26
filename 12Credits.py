#! /usr/bin/env python3
import os
import pwd
print("Process ID: {0}".format(os.getpid()))
print("Parent Process ID: {0}".format(os.getppid()))
print("Session ID: {0}".format(os.getsid(0)))
print("Process Group ID: {0}".format(os.getpgrp()))
print("User ID: {0}".format(os.getuid()))
print("User Name: {0}".format(pwd.getpwuid(os.getuid()).pw_name))
print("Effective User ID: {0}".format(os.geteuid()))
print("Effective User Name: {0}".format(pwd.getpwuid(os.geteuid()).pw_name))
