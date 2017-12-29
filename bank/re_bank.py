import requests
from bs4 import BeautifulSoup
import pandas
import csv
# 連結
payload = {
    'from':'/bbs/Gossiping/index.html',
    'yes':'yes'
}
# rs = requests.session()
# res = rs.post('https://www.ptt.cc/ask/over18', verify = False , data = payload) 回覆POST封包 
# res = rs.get('https://www.ptt.cc/bbs/Gossiping/index.html', verify = False) 回覆get封包
# res.text

url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
rs = requests.session()
res = rs.post('https://www.ptt.cc/ask/over18', verify = False , data = payload)
res = rs.get(url, verify = False)
# res.text

soup = BeautifulSoup(res.text, 'html.parser')
tag_name = 'div.title a'
articles = soup.select(tag_name)
# for art in articles:
#     print(art['href'],art.text)

paging = soup.select("div.btn-group-paging a")
# print(paging)
page2_url = paging[1]["href"]

res2 = requests.get('http://www.ptt.cc'+page2_url)
# next_url = 'http://www.ptt.cc'+ paging[1]["href"]

print(page2_url)
# print(next_url)
# print(res2)
