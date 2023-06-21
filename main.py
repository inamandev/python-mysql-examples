import mysql.connector
import helper
host = "db"
user = "root"
password = "password"


db = mysql.connector.connect(
  host=host,
  user=user,
  password=password
)

# check if database is connected
if not helper.check_if_connected(db):
  print("mysql not connected")

# getting to cursor to operate
client = db.cursor()

# create new database if does not exist
if not helper.check_database_exist("persons", client):
  helper.create_database(client, "persons")
