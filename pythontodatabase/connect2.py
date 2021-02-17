import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    auth_plugin='mysql_native_password',
    database='pythondecember'
)

cursor=db.cursor()
sql="create table movie (id int,name varchar(20),year varchar(20),rating int)"
cursor.execute(sql)
print("table created")
db.close()