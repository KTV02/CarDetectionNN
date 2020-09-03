import os



def getBlacklist():
    blacklist=[]
    if os.path.isfile('blacklist.txt'):
        file=open("blacklist.txt","r")
        alllines=file.readlines()
        for i in alllines:	
            blacklist.append(i)
    return blacklist

def clean(urls):
    blacklist=[]
    for i in urls:
        if "&pageNumber" in i:
            blacklist.append(i.split("&pageNumber")[0])
    #print(blacklist)
    return blacklist


def write(blacklist):
    file=open("blacklist.txt","a")
    file.write("\n")
    for i in blacklist:
        file.write(i)
        file.write("\n")



write(clean(getBlacklist()))
