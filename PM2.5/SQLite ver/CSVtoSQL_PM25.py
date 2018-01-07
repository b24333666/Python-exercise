import requests
import sqlite3

html = requests.get("http://opendata.epa.gov.tw/ws/Data/ATM00625/?$format=csv")
html.encoding = "UTF-8"

conn = sqlite3.connect("PM25.db")
cursor = conn.cursor()
sqlstr = "create table if not exists PM25_1 (num integer primary key autoincrement not null,\
 'Site' text, 'county' text, 'PM_25' text, 'DataCreationDate' text )"
cursor.execute (sqlstr)

list1 = html.text.split("\r\n")
print("測站名稱\t縣市名稱\t細懸浮微粒濃度(PM2.5)\t資料建置日期")
for i in range(1,len(list1)-1):
    list2 = list1[i].split(",")
    print(list2[0]+"\t"+list2[1]+"\t"+list2[2]+"\t"+list2[3])
    sqlstr_1 = "insert into PM25_1(Site,county,PM_25,DataCreationDate) values\
    ('"+str(list2[0])+"','"+str(list2[1])+"','"+str(list2[2])+"','"+str(list2[3])+"')"
    # sqlstr_1 = "insert into PM25_1(Site,county,PM_25,DataCreationDate) value ('keelung','keelung','20','2018-02-01')"
    cursor.execute(sqlstr_1)
    conn.commit()
conn.close()
#   SQL           重複1次                                   重複出現超過一次的資料
# SELECT PM_25,COUNT(1)FROM PM25_1 GROUP BY DataCreationDate &&  HAVING COUNT(*) > 1 
    


