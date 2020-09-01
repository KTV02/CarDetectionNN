#!/usr/bin/python
import os
from time import sleep
import sys
def checkPid():
    f=open("/media/hdd1/tools/carProject/pid.txt","r")
    pid=int(f.read())
    try:
        os.kill(pid,0)
    except OSError:
        print("Crawler is not running -> starting")
	os.system("pkill -f 'firefox-esr'")
        os.system("python /media/hdd1/tools/carProject/mobiledeCRAWLER.py > /media/hdd1/tools/carProject/crawler.txt")
    else:
        print("Crawler is still running")
        return True
checkPid()
