from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()

def getlinks(pageurl):
    global pages
    html = urlopen(r"https://zh.wikipedia.org/"+pageurl)
    bsobj = BeautifulSoup(html)
    for link in bsobj.findAll("a",href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newpages = link.attrs['href']
                print(newpages)
                pages.add(newpages)
                getlinks(newpages)
getlinks("")