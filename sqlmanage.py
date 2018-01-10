from django.db import connection
import django.db
from django import request
from MySQLdb import cursor
from datetime import datetime
import MySQLdb

# 這裡都是views.py
# SQL table is article
# 讀取資料庫傳給Templates
# with as語法 
def index(request):
    with connection.cursor()as cursor:
        cursor.execute("select * form article")
        row = cursor.fetchall()
    return render(request,index.html,{'datas':article})# 原本{'datas':articles}

# 接收表單到資料庫
def create(request):
    if request.method == "POST":
        title = request.POST['title'] # title是指從表單接收到的ID名稱
        content = request.POST['content'] # content是指從表單接收到的ID名稱
        with connection.cursor() as cursor:
            sql = """insert into article(title,content,pudDateTime)values(%s,%s,%s)"""
            cursor.execute(sql,(title,content,srt(datetime.now()))) #執行上行SQL語法
        return redirect('/') # 新增完成後傳回給redirect函式 
    return render(request,'create.html')# if函式使用!! 如果不是POST傳送過來呼叫轉送至Templates/Cerate.html

# 刪除資料
def delete(request,id):
    with connection.cursor() as cursor:
        sql = """delete from article_article where id=%s"""
        cursor.execute(sql,(id,))
    return redirect('/')

# delete is urls.py
# urlpatterns = [
#     path('delete/<int:id>',views.delete,name='delete')
# ]


# 接收修改表單到資料庫
def update(request,id=None):
    if request.method == "POST":
        with connection.cursor() as cursor:
            sql ="""update article_article set title=%s, contnet=%s where id=%s"""
            cursor.execute(sql,(title,contnet,id))
        return redirect('/')

    with connection.cursor() as cursor:
        sql = """select * from article_article where id=%s"""
        cursor.execute(sql,(id,))
        row = cursor.fetchone()
    return render(request,'edit.html',{'article':d})

