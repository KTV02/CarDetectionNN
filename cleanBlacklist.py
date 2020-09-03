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
    ids=[]
    #check for every listening if its a "normal" listing with id in url
    for i in urls:
        if "?id=" in i:
            #if id is in url cut it and save it in list ids
            ids.append(i[51:60])
            ids.append(i)
    return ids
 

def write(blacklist):
    file=open("blacklist.txt","a")
    file.write("\n")
    file.write("\n")
    file.write("\n")
    file.write("\n")
    file.write("\n")
    file.write("\n")
    file.write("\n")
    file.write("\n")
    file.write("\n")
    file.write("\n")
    for i in blacklist:
        file.write(i)



write(clean(getBlacklist()))
