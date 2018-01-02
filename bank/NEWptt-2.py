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
if not os.path.isdir('download'):
    os.mkdir('download')
url = 'https://www.ptt.cc/bbs/'+x+'/index.html'
reg_imgur_file = re.compile('http[s]?://[i.]*imgur.com/(\w+\.(?:jpg|png|gif))')
reg_img_file = re.compile('(?:jpg|png|gif)')
for round in range(1):
    rs = requests.session()
    res = rs.post('https://www.ptt.cc/ask/over18', verify = False , data = payload)
    res = rs.get(url, verify = False)
    soup = BeautifulSoup(res.text, 'html.parser')
    tag_name = 'div.title a'
    articles = soup.select(tag_name)
    paging = soup.select("div.btn-group-paging a")
    next_url = 'http://www.ptt.cc'+paging[1]['href']
    url = next_url
    # print("url: " + url)
    for article in articles:
        print(article.text,article['href'])
        if not os.path.isdir(os.path.join('download',article.text)):
            try:
                os.mkdir(os.path.join('download',article.text))
                # os.mkdir(os.path.join('download',article.text.replace(":", "：").replace("?", "？")))
            except Exception as e:
                print(e)
                print(e.args)
                continue
        res = requests.get('http://www.ptt.cc'+ article['href'])
        images = reg_imgur_file.findall(res.text)
        print(images)
        for image in set(images):
            # ID =re.search('\w+\.(?:jpg|png|gif)',image).group(1)
            # ID = reg_img_file.findall(image)
            # print(ID[0])
            print(image)
            urlretrieve("http://i.imgur.com/" + image,os.path.join('download',article.text,image))
            break
        break