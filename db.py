import mysql.connector
con = mysql.connector.connect(host="localhost",user="root",password="")
cur= con.cursor()
try:
    cur.execute("create database mca")

except:
    con.rollback()
con.close()