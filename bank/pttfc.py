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
def crawler():
    if not os.path.isdir('download'):
        os.mkdir('download')
    x = str(input("請輸入你要進入的看板英文名稱: "))
    url = 'https://www.ptt.cc/bbs/'+x+'/index.html'
    for round in range(3):

    # 回傳滿18歲資訊 封包形式為POST
        # rs = requests.session()
        # res = rs.post('https://www.ptt.cc/ask/over18', verify = False , data = payload)
        # res = rs.get(url, verify = False)
    # 
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        tag_name = 'div.title a'
        articles = soup.select(tag_name)
        # for art in articles:
        #     print(art['href'],art.text)
        paging = soup.select("div.btn-group-paging a")
        next_url = 'http://www.ptt.cc'+paging[1]['href']
        url = next_url 
        print(url)
        download_images(articles)


def download_images(articles):
    for article in articles:
        print(article.text,article['href'])
        if not os.path.isdir(os.path.join('download',article.text)):
            os.mkdir(os.path.join('download',article.text))
        res = requests.get('http://www.ptt.cc'+ article['href'])
        images = reg_imgur_file.findall(res.text)
        print(images)

        for image in set(images):
            ID = re.search('http[s]?://[i.]*imgur.com/(\w+\.(?:jpg|png|gif))',image).group(1)
            print(ID)
            urlretrieve(image,os.path.join('download',article.text,ID))

reg_imgur_file = re.compile('http[s]?://[i.]*imgur.com/(\w+\.?:(jpg|png|gif))')
crawler()