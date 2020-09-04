# dupFinder.py
import os, sys
import hashlib
from time import sleep
 
def opener():
    lines=[]
    file=open("imageDuplicates.txt","r")
    for line in file:
        lines.append(line)
    return lines


def remove(lines):
    deleted=[]
    for path in lines:
        url1,url2=path.split("and")
        url1=url1.replace("Duplicate found:","")
        url2=url2.replace("and","")
        url1=url1.replace(" ","")
        url2=url2.replace(" ","")
        url2=url2.replace("\n","")
        if not url1 in deleted and not url2 in deleted:
            deleted.append(url1)
            #print("deleted",url1)
            #print("total",deleted)
            try:
                os.remove(url1)
            except:
                continue

remove(opener())
