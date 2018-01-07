import requests
import sqlite3
import time
import os


# if not os.path.isdir('PM25'):
#     os.mkdir('PM25')
html = requests.get("http://opendata.epa.gov.tw/ws/Data/ATM00625/?$format=csv")
html.encoding = "UTF-8"
dateName = time.strftime("%y%m%d")
conn = sqlite3.connect("PM25"+dateName+".db")
cursor = conn.cursor()

try:
    # if not os.path.isdir(os.path.join('PM25',article.text)):
    #     os.mkdir(os.path.join('PM25',article.text))
    sqlstr = "create table if not exists PM25"+str(dateName)+" (num integer primary key autoincrement not null,\
    'Site' text , 'county' text , 'PM_25' text, 'DataCreationDate' text )"
    sqlstr_1 = "create unique index PM251 on PM25"+str(dateName)+" ('Site', 'DataCreationDate')"
    cursor.execute (sqlstr)
    cursor.execute (sqlstr_1)
except Exception as e:
    print(e)

list1 = html.text.split("\r\n")
print("測站名稱\t縣市名稱\t細懸浮微粒濃度(PM2.5)\t資料建置日期")
count=0
for i in range(1,len(list1)-1):
    list2 = list1[i].split(",")
    print(list2[0]+"\t"+list2[1]+"\t"+list2[2]+"\t"+list2[3])
    sqlstr_2 = "replace INTO PM25"+str(dateName)+"(Site,county,PM_25,DataCreationDate) values\
    ('"+str(list2[0])+"','"+str(list2[1])+"','"+str(list2[2])+"','"+str(list2[3])+"')"
    count += 1
    cursor.execute(sqlstr_2)
    conn.commit()
    print("已輸入第"+str(count)+"筆資料!!")
conn.close()
