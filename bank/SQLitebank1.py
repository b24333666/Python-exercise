import requests
import sqlite3
import pandas
from bs4 import BeautifulSoup
import re

reg = requests.get('https://coinmarketcap.com/currencies/bitcoin/')
# print(reg)
bsoup = BeautifulSoup(reg.text,'html.parser')

soup =bsoup.find_all("span")
# soup =type(bsoup.select('span'))
print(soup)
# m = re.search('<span data-usd="(.*?)"',soup)
# mp = m.group(1)
# print(m)
# <span class="price" data-usd="16937.5" data-btc="1.00485" data-native="0.00101903">
