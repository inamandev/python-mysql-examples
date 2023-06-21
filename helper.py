
def check_if_connected(db):
  print("check if mysql is connected")
  return db.is_connected()

def check_database_exist(database, client):
  print("check if database exist")
  exist = False
  client.execute("SHOW DATABASES")
  db_names = client.fetchall()
  for db_name in db_names:
    if db_name[0] == database:
      print("database "+ database +" already exist")
      exist = True
      break
  return exist
  
def create_database(client, database = "my_database"):
  print("create new database with name " + database)
  client.execute("CREATE DATABASE " + database)

def check_table_exist(client, table = "my_table"):
  print("check if table exist")
  exist = False
  client.execute("SHOW TABLES")
  table_names = client.fetchall()
  for table_name in table_names:
    if table_name[0] == table:
      print("table "+ table +" already exist")
      exist = True
      break
  return exist

def create_persons_table(client):
  print("create new table persons")
  client.execute("CREATE TABLE persons (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255), age INT)")