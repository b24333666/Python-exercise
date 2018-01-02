import requests
from bs4 import BeautifulSoup
import re
from urllib.request import urlretrieve
import os

def Get_web(target):
    html = requests.get(target)

    soup = BeautifulSoup(html.text,'html.parser')

    article_link = soup.select('div.title a')

    article_data = soup.select('div.data')

    return soup,article_link,article_data


def Download(article_link,article_data):
    reg_imgur_file = re.compile('http[s]?://[i.]*imgur.com/(\w+\.(?:jpg|png|gif))')

    for art,art_data in zip(article_data,article_link):

        if artdata.text == data:
            
            print(art['herf'],herf.text)

            html_article = requests.get('https://www.ptt.cc'+art['herf'] )

            images = reg_imgur_file.findall(html_article.text)

            path = 'D:\\'+art.text
            os.mkdir(path)

            for image in set(images):
                ID = re.search('http[s]?://[i.]*imgur.com/(\w+\.(?:jpg|png|gif))',image).group(1)
                print(ID)
                urlretrieve(image,path+'\\'+ID)

def Lastpage(Soup):
    page = soup.select('div.btn-group-paging a')

    pagingLast = paging[1]['href']

    url_last = 'https://www.ptt.cc'+pagingLast
    target = url_last
    return target



