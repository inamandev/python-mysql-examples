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
client = db.cursor(dictionary=True)

# create new database if does not exist
if not helper.check_database_exist("persons", client):
  helper.create_database(client, "persons")

# selecting database to work with
client.execute("USE persons")

# create new table if does not exist
if not helper.check_table_exist(client, "persons", "persons"):
  helper.create_persons_table(client)

# insert initial records if table has not records at all
if not helper.check_if_records_exist(client, "persons"):
  helper.insert_initial_records(client, "persons")
  db.commit
  print("{} records inserted successfully".format(client.rowcount))

# select records from existing records
print("below are all records in persons table")
for row in helper.select_all_existing_records(client, "persons"):
  print("Id: {}, Name: {}, Address: {}, Age: {}".format(row["id"], row["name"],row["address"],row["age"]))

# select one specific record from table
person = helper.select_one(client, "persons", 3)
print("Name of the record is {} and age is {}".format(person["name"], person["age"]))