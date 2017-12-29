import os
import hashlib
import ast
import sqlite3
import requests
from bs4 import BeautifulSoup
import csv

conn = sqlite3.connect('database_exchang.sqlite')
# 
cursor = conn.cursor()
# 

sqlstr = '''
CREATE TABLE IF NOT EXISTS TableBank_exchang ("NO"
INTEGER PRIMARY KEY AUTOINCREMENT
NOT NULL UNIQUE ,"Site NAME" TEXT NOT NULL ,"Bank_exchang" INTEGER)
'''

cursor.execute(sqlstr)
# 目標網址
url = "http://rate.bot.com.tw/xrt?Lang=zh-TW"
# 擷取HTML原始碼
html = requests.get(url).text.encode('UTF-8-sig')

# 檢查MD5
md5 = hashlib.md5(html).hexdigest()
old_md5 = ""
if  os.path.exists('old_md5.txt'):
    with open('old_md5.txt', 'r') as f:
        old_md5 = f.read()

with open('old_md5.txt', 'w') as f:
    f.write(md5)

if md5 != old_md5 :
    print('already updata....')
    sp = BeautifulSoup(html,'html.parser')
    jsondata = ast.literal_eval(sp.text)
    conn.execute("delete from TableBank_exchang")
    conn.commit()

# 計算迴圈次數
    n = 1
    for site in jsondata:
        SiteName = site["SiteName"]
        Bank_exchang = 0 if site ["Bank_exchang"] == "" else float(site["Bank_exchang"])
        print("美元:{}  新台幣:{}".format(SiteName,Bank_exchang))
        # 
        sqlstr = "insert into TableBank_exchang values({}、'{}'、{})".format(n,SiteName,Bank_exchang)
        cursor.execute(sqlstr)
        n += 1
        conn.commit()

else:
    print('資料庫未更新,從資料庫讀取中...')
    cursor = conn.execute("select * from TableBank_exchang")
    rows = cursor.fetchall()
    for row in rows:
        print("美元:{}  新台幣:{}".format(row[1],row[2]))

conn.close()
# 關閉資料庫連線

