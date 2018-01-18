from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random
from urllib.parse import urlparse


pages = set()
random.seed(datetime.datetime.now())

def getinternallinks(bsobj,includeurl):
    internallinks = []

    for link in bsobj.findAll("a",href=re.compile("^(/|.*" + includeurl + ")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internallinks:
                internallinks.append(link.attrs['href'])
    return internallinks

def getexternallinks(bsobj,excludeurl):
    externallinks = []

    for link in bsobj.findAll("a",href=re.compile("^(http|WWW)((?!" + excludeurl + ").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externallinks:
                externallinks.append(link.attrs['href'])
    return externallinks

def splitaddres(addres):
    addresparts = addres.replace("http://","").split("/")
    return addresparts

def getrandomexternallinks(startingpage):
    html = urlopen(startingpage)
    bsobj = BeautifulSoup(html)
    externallinks = getexternallinks(bsobj,urlparse(startingpage).netloc)
    if len(externallinks) == 0:
        print("")
        domain = urlparse(startingpage).scheme + "://" + urlparse(startingpage).netloc
        internallinks = getinternallinks(bsobj,domain)
        return getrandomexternallinks(internallinks[random.randint(0,len(internallinks)-1)])

    else:
        return externallinks[random.randint(0,len(externallinks)-1)]

def followexternalomly(startingsite):
    externallink = getrandomexternallinks("http://oreilly.com")
    print("random external link is: "+ externallink)
    followexternalomly(externallink)

followexternalomly("http://oreilly.com")

