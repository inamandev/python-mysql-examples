
def check_if_connected(db):
  print("check if mysql is connected")
  return db.is_connected()

def check_database_exist(database, client):
  print("check if database exist")
  exist = False
  client.execute("SHOW DATABASES")
  db_names = client.fetchall()
  for db_name in db_names:
    if db_name["Database"] == database:
      print("database "+ database +" already exist")
      exist = True
      break
  return exist
  
def create_database(client, database = "my_database"):
  print("create new database with name " + database)
  client.execute("CREATE DATABASE " + database)

def check_table_exist(client, table = "my_table", database = "my_database"):
  print("check if table exist")
  exist = False
  client.execute("SHOW TABLES")
  table_names = client.fetchall()
  for table_name in table_names:
    if table_name["Tables_in_"+database] == table:
      print("table "+ table +" already exist")
      exist = True
      break
  return exist

def create_persons_table(client):
  print("create new table persons")
  client.execute("CREATE TABLE persons (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255), age INT)")

def check_if_records_exist(client, table):
  print("check if any records exist in table "+ table)
  exist = False
  client.execute("SELECT count(id) AS total FROM " + table)
  count = client.fetchall()
  print("{} records exist in table {}".format(count, table))
  if count[0]["total"] > 0:
    print("{} records exist in table {}".format(count[0][0], table))
    exist = True

  return exist

def insert_initial_records(client, table):
  print("inserting initial records to table " + table)
  sql = "INSERT INTO " + table + " (name, address, age) VALUES (%s, %s, %s)"
  data = [
    ("Ramesh", "Address 1", 13),
    ("Amy", "Address 2", 14),
    ("Peter", "Address 3", 28),
    ("Rani","Address 4", 43)
  ]
  client.executemany(sql, data)

def select_all_existing_records(client, table):
  client.execute("SELECT * FROM " + table)
  return client.fetchall()

def select_one(client, table, id):
  sql = "SELECT * FROM "+ table+" WHERE id = %s"
  data = (id,)
  client.execute(sql, data)
  return client.fetchone()