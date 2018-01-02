import sqlite3
import re

conn = sqlite3.connect('test.db')
cursor =  conn.cursor()
# create創造表格
def create():
    if not cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')

# data_enty寫入
# 寫入前請勿開啟SQL表格 會無法寫入
#   cursor.execute("insert into user values (2, 'Json')")<====SQL寫入語法
#   conn.commit()<====commit提送回conn
# 最後要記得關閉cursor和conn 順序為先進後出

def data_enty():
    cursor.execute("insert into user values (2, 'Json')")
    conn.commit()
    cursor.close()
    conn.close()

# create()
data_enty()


