import pymysql
conn = pymysql.connect(host="localhost",user="root",password="",database="python1")
cursor = conn.cursor()

insert = "INSERT INTO table1(name,rollno) VALUES('prit',1)"
cursor.execute(insert)
conn.commit()
conn.close()
