
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
      exist = True
      break
  return exist
  
def create_database(client, database = "my_database"):
  print("create new database with name " + database)
  client.execute("CREATE DATABASE " + database)
