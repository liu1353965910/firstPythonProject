# -*- coding: UTF-8 -*-

import pymysql.cursors

connection = pymysql.connect(host="47.106.85.176",
                             user="root",
                             password="lqw2580.",
                             db="PlaneDB",
                             charset="utf8mb4",
                             cursorclass=pymysql.cursors.DictCursor)
try:
    with connection.cursor() as cursor:
        sql = "select * from Booking"
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()



