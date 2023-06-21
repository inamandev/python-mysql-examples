import mysql.connector

host = "db"
user = "root"
password = "password"


mydb = mysql.connector.connect(
  host=host,
  user=user,
  password=password
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")
print("showing databases")
for x in mycursor:
  print(x) 