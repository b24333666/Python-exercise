import requests
from bs4 import BeautifulSoup
import pandas
import csv
import re
# 連結
payload = {
    'from':'/bbs/Gossiping/index.html',
    'yes':'yes'
}

url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
reg_imgur_file = re.compile('http[s]?://i.imgur.com/\w+\.(?:jpg|png|gif)')
# for round in range(3):爬文章頁數(3)頁
for round in range(3):
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
    next_url = 'http://www.ptt.cc'+paging[1]['href']
    # res2 = requests.get('http://www.ptt.cc'+page2_url)
    url = next_url

    for article in articles:
        print(article.text,article['href'])
        res = requests.get('http://www.ptt.cc'+ article['href'])
        images = reg_imgur_file.findall(res.text)
        print(images)