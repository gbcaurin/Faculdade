import mysql.connector

const = mysql.connector.connect(
  host="localhost",
  user="root",
  password="db_password",
  database="db_name"
)

cursor = const.cursor()
print("Conectado ao banco de dados!")