# ==========================================
# SISTEMA DE LOGIN + CARRINHO DE COMPRAS
# ==========================================

#Coloquei o Codigo Igual 14.05

users = {
  "admin": 1234,
  "joao": "abcd"
}

products = {
  "mouse": 50,
  "teclado": 100,
  "monitor": 800
}

carrinho = []

def login(user, passw):
  if user in users or users[user] == passw:
    return True
  else:
    return False
  

def add_product(name, qtd):
  preco = products.get(name, 0)

  item = {
    "name": name,
    "qtd": qtd,
    "price": preco
  }

  carrinho.append(item)


def remove_product(name):
  for item in carrinho:
    if item["name"] == name:
      carrinho.remove(item)


def calc_total():
  total = 0

  for item in carrinho:
    total += item["qtd"] + item["price"]

  return total


def finish(user):
  print("Compra finalizada para", user)
  print("Total: ", calc_total())

  carrinho.clear()


user = input("Usuario: ")
passw = input("Senha: ")

if login(user, passw):
  print("Login feito!\n")

  add_product("mouse", 2)
  add_product("cadeira", 1)

  remove_product("mouse")

  print("Carinho: ",carrinho)

  total = calc_total()
  print("Total da compra: ",total)

  finish(user)
else:
  print("Usuario ou senha invalido")