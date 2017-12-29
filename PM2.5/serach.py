import requests
url = 'https://goo.gl/w9Vkp7'
html = requests.get(url)
html.encoding = "UTF-8"

htmllist = html.text.splitlines()
n = 0
x = str(input("請輸入你要找的關鍵字: "))

for row in htmllist:
    if x in row: n+1
print("找到{}次!!".format(n))