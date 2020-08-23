import pymysql
con=pymysql.connect(host="localhost",user="root",password="",database="mca")
cur= con.cursor()
cur.execute("SELECT *FROM student")
r =cur.fetchall()
print(r)
con.commit()
con.close()