import requests
url = 'https://taqm.epa.gov.tw/pm25/tw/PM25A.aspx?area=1'
html = requests.get(url)
html.encoding = "UTF-8"
htmllist = html.text.splitlines()
for row in htmllist:
    print(row)