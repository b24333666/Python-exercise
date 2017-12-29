import requests
from bs4 import BeautifulSoup 
url = "https://taqm.epa.gov.tw/pm25/tw/PM25A.aspx?area=1"
html = requests.get(url)
sp = BeautifulSoup(html.text,'html.parser')

print(sp)