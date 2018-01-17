# from bs4 import BeautifulSoup
# import requests as req
# import json
# import string
# import pandas 
import re

# # https://www.coingecko.com/chart/279/twd.json?locale=zh-tw

# url = 'https://www.coingecko.com/chart/279/twd.json'

# html = req.get(url)
# # print(html)
# html.encoding = 'UTF-8'
# soup = BeautifulSoup(html.text,'html.parser')
# jl = json.loads(str(soup))
# # print(jl)
# for stats in jl['stats']:
#     print(stats[str(1438905600000.0)])


x = re.compile('a(?=.*/d)')
y = 'a9'
z = re.match(x,y)
print(z)


x1 = re.compile('a(?=/d.*)')
y1 = 'a9'
z1 = re.match(x1,y1)
print(z1)






# x= lambda a9 : re.compile('.*[0-9]'),re.match()
# print(x)

# print(soup)
# bssoup = soup.findAll ()







# getdict = sl.values()
# def dict_get(self,**oi):
#     for i in oi:
#         for v in i:
#             for vr in v :
#                 print(vr)
#                 return vr

        

            

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