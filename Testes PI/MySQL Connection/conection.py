import mysql.connector

const = mysql.connector.connect(
  host="localhost",
  user="root",
  password="0711",
  database="teste"
)

cursor = const.cursor()

def create_user(name, email, password):
  sql = "INSERT INTO users (user_name, user_email, user_pass) VALUES (%s, %s, %s)"
  valores = (name, email, password)
  cursor.execute(sql, valores)
  const.commit()
  print("Usuário criado com sucesso!")

def edit_user(id, name, email, password):
  sql = "UPDATE users SET user_name = %s, user_email = %s, user_pass = %s WHERE id = %s"
  valores = (name, email, password, id)
  cursor.execute(sql, valores)
  const.commit()
  print("Usuário editado com sucesso!")

def delete_user(id):
  sql = "DELETE FROM users WHERE id = %s"
  valor = (id)
  cursor.execute(sql, valor)
  const.commit()
  print("Usuário deletado com sucesso!")

def list_users():
  sql = "SELECT * FROM users"
  cursor.execute(sql)
  result = cursor.fetchall()
  print("Lista de usuários:")
  for user in result:
    print(f"ID: {user[0]} | Nome: {user[1]} | Email: {user[2]} | Senha: {user[3]}")

print("Conectado ao banco de dados!")
