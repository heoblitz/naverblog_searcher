#!/usr/bin/python3
import psutil
import time
import re
import os

while(1):
	used = psutil.virtual_memory()[2]
	if(used > 80):
		os.system('pkill chromium')
		print('pkill chromium')
		os.system('ps aux | grep chrome | awk \' { print $2 } \' | xargs kill -9')
		print('pkill chrome')
		os.system('ps aux | grep main.py | awk \' { print $2 } \' | xargs kill -9')
		print('pkill main.py')	
	time.sleep(1)

