import requests
from bs4 import BeautifulSoup
import pandas
import os
import re
from urllib.request import urlretrieve

# 連結
payload = {
    'from':'/bbs/Gossiping/index.html',
    'yes':'yes'
}
x = str(input("請輸入你要進入的看板英文名稱: "))
# url = 'https://www.ptt.cc/bbs/'+x+'/index.html'
# reg_imgur_file = re.compile('http[s]?://[i.]*imgur.com/(\w+\.(?:jpg|png|gif))')

# def downloadimg(articles):
#         for article in articles:
#         print(article.text,article['href'])
#         is not os.path.isdir(os.path.join('download',article.text)):
#             os.mkdir(os.path.join('download',article.text))
#         res = requests.get('http://www.ptt.cc'+ article['href'])
#         images = reg_imgur_file.findall(res.text)
#         print(images)
#         for image in set(images):
#             ID =re.search('http[s]?://[i.]*imgur.com/(\w+\.(?:jpg|png|gif))',image).group(1)
#             print(ID)
#             urlretrieve(image,os.path.join('download',article.text,ID))
# for round in range(3):爬文章頁數(3)頁

if not os.path.isdir('download'):
    os.mkdir('download')
url = 'https://www.ptt.cc/bbs/'+x+'/index.html'
reg_imgur_file = re.compile('http[s]?://[i.]*imgur.com/(\w+\.(?:jpg|png|gif))')
for round in range(3):
    rs = requests.session()
    res = rs.post('https://www.ptt.cc/ask/over18', verify = False , data = payload)
    res = rs.get(url, verify = False)
    soup = BeautifulSoup(res.text, 'html.parser')
    tag_name = 'div.title a'
    articles = soup.select(tag_name)
    # for art in articles:
    #     print(art['href'],art.text)
    paging = soup.select("div.btn-group-paging a")
    next_url = 'http://www.ptt.cc'+paging[1]['href']
    url = next_url  
    # downloadimg(articles)
    for article in articles:
        print(article.text,article['href'])
        if not os.path.isdir(os.path.join('download',article.text)):
            os.mkdir(os.path.join('download',article.text))
        res = requests.get('http://www.ptt.cc'+ article['href'])
        images = reg_imgur_file.findall(res.text)
        print(images)
        for image in set(images):
            ID =re.search('http[s]?://[i.]*imgur.com/(\w+\.(?:jpg|png|gif))',image).group(1)
            print(ID)
            urlretrieve(image,os.path.join('download',article.text,ID))
