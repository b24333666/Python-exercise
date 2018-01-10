from bs4 import BeautifulSoup
import requests as req
import json
import string

# https://www.coingecko.com/chart/279/twd.json?locale=zh-tw

url = 'https://www.coingecko.com/chart/279/twd.json'

html = req.get(url)
# print(html)
html.encoding = 'UTF-8'
soup = BeautifulSoup(html.text,'html.parser').text
# print(soup)
sl = json.loads(str(soup))
# print(type(sl))
getdict = sl.values()
def dict_get(self,**oi):
    for i in oi:
        for v in i:
            for vr in v:
                print()
            print()
        return vr
        
nv = dict_get(getdict)
print(nv)
            

# v = dict_get(getdict)
# print(v)

# print(type(getdict))
# print(getdict)
# for i in range(1,len(getdict)):
#     print(i)

# for i in getdict:
#     for v in i:
#         rv = repr(v)
#         # print(rv[0]+"\t"+rv[1])
#         print(rv,end=' ')
#     print()
#  v = v.replace('')
# print(v)    


# soupdoc = soup.find_all('dict').get.text

# print(soupdoc)


