import requests
import json 



# print(jsondata)
def PM25JSON():
    for site in jsondata:
        county = site["county"]
        Sitename = site["Site"]
        PM25 = site["PM25"]
        ItemUnit = site["ItemUnit"]
        DataCreationDate = site["DataCreationDate"]
        print("{0}{1}\tPM2.5:\t{2}\t{3}\t建置日期:{4}".format(county,Sitename,PM25,ItemUnit,DataCreationDate))

url = requests.get("http://opendata.epa.gov.tw/ws/Data/ATM00625/?$format=json")
url.encoding = "UTF-8"
jsondata = eval(url.text)

PM25JSON()