import hashlib
import requests
import os
# import sqlite3 轉MySQL
import time
import MySQLdb


# if not os.path.isdir('PM25'):
#     os.mkdir('PM25')
# ===========================PM_2.5================================
url = "http://opendata.epa.gov.tw/ws/Data/ATM00625/?$format=csv"
html = requests.get(url)
html.encoding = "UTF-8"
dateName = time.strftime("%y%m%d")

conn = MySQLdb.connect("127.0.0.1","root","root","PM25",use_unicode=True, charset="utf8mb4")
# conn = MySQLdb.connect("PM25" + dateName + ".mwb")
#                       ("SQL位置","SQL帳號","SQL密碼","Table Name",開啟萬國碼, 設定編碼為utf8) 後面兩項沒開會跳出
#                       UnicodeEncodeError: ‘latin-1’ codec can’t encode characters in position 44-46: ordinal not in range(256)
cursor = conn.cursor()
# ===========================MD5檢驗=================================
md5 = hashlib.md5()
# md5.update(b'Test string!') Test MD5功能用
# print("目前MD5為:"+ md5)
# ===================================================================

html_1 = requests.get(url).text.encode('UTF-8-sig')
# 判斷網頁是否更新
md5 = hashlib.md5(html_1).hexdigest()
print("目前MD5為:"+ md5)


#透過OS的PATH變數新增old_md5.txt文字檔
if os.path.exists('old_md5.txt'): 
    # 開啟old_md5.txt 並為r 讀取狀態
    global old_md5#後面迴圈有old_md5偶發抓不到的問題

    with open('old_md5.txt', 'r') as f: 
        old_md5 = f.read()
    # 開啟old_md5.txt 並為w 寫入狀態
    with open('old_md5.txt', 'w') as f: 
        f.write(md5)
# 如果已存在old_md5.txt則開啟old_md5.txt 並為w 寫入新MD5並覆蓋舊有MD5
else:
    with open('old_md5.txt', 'w') as f: 
        f.write(md5)
# ===========================比對MD5新舊================================
# 新MD5與舊MD5一樣時為不更新狀態
if md5 == old_md5: 
    print("尚未有新資料加入，請等候...")
else:
    try:
        # if not os.path.isdir(os.path.join('PM25',article.text)):
        #     os.mkdir(os.path.join('PM25',article.text))
        print("資料未更新，正在從網路更新ing")
        sqlstr = "CREATE IF NOT EXISTS TABLE pm25\
                `(num` INT NOT NULL AUTO_INCREMENT,\
                `Site` VARCHAR(10) NOT NULL,\
                `county` VARCHAR(45) NOT NULL,\
                `PM_25` VARCHAR(45) NULL,\
                `DataCreationDate` VARCHAR(45) NULL,\
                 PRIMARY KEY (`num`),\
                UNIQUE INDEX `Site_UNIQUE` (`Site` ASC),\
                UNIQUE INDEX `DataCreationDate_UNIQUE` (`DataCreationDate` ASC));"
        # 上面是MySQL語法
        cursor.execute (sqlstr)

    except Exception as e:
        print(e)

    list1 = html.text.split("\r\n")
    print("測站名稱\t縣市名稱\t細懸浮微粒濃度(PM2.5)\t資料建置日期")
    count=0
    for i in range(1,len(list1)-1):#一定要Len(list)-1否則會出現讀取資料超出範圍一格
        list2 = list1[i].split(",")
        print(list2[0]+"\t"+list2[1]+"\t"+list2[2]+"\t"+list2[3])
        sqlstr_2 = "replace into PM25(Site,county,PM_25,DataCreationDate) values\
        ('"+str(list2[0])+"','"+str(list2[1])+"','"+str(list2[2])+"','"+str(list2[3])+"');"
        count += 1
        cursor.execute(sqlstr_2)
        conn.commit()
        print("已輸入第"+str(count)+"筆資料!!")
    conn.close()