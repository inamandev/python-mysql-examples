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

# selecting database to work with
client.execute("USE persons")

# create new table if does not exist
if not helper.check_table_exist(client, "persons"):
  helper.create_persons_table(client)

if not helper.check_if_records_exist(client, "persons"):
  helper.insert_initial_records(client, "persons")
  db.commit
  print("{} records inserted successfully".format(client.rowcount))