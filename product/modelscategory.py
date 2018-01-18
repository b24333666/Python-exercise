from django.db import connection

class Category:
    def all(self):
        with connection.cursor() as cursor:
            cursor.execute("select * from pm25")
            datas = cursor.fetchall()
        return datas