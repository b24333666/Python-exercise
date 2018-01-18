from django.db import connection

class Product:
    def all(self):
        with connection.cursor() as cursor:
            cursor.execute("select * from pm25")
            datas = cursor.fetchall()
        return datas
    
    def single(self,id):
        with connection.cursor() as cursor:
            cursor.execute("select * from pm25 where num=%s",(id,))
            data = cursor.fetchone()
        return data

    def create(self,product):
        with connection.cursor() as cursor:
            sql = """INSERT INTO pm25(num,Site,county,PM_25,DataCreationDate)
                     VALUES(%s,%s,%s,%s)"""
            cursor.execute(sql,product)

    def update(self,product):
        with connection.cursor() as cursor:
            sql = """UPDATE pm25 set num=%s,Site=%s,county=%s,PM_25=%s,DataCreationDate=%s
                     where num=%s"""
            cursor.execute(sql,product)

    def delete(self, id):
        with connection.cursor() as cursor:
            sql = "delete from pm25 where num=%s"
            cursor.execute(sql,(id,))
    
    