#1 - Crie um dicionario vazio
users = {}
#2 - Inserir 10 elementos no dicionario com a chave nome e valores idade e cidade
for i in range(10):
  nome = input("Digite seu nome: ")
  idade = int(input("Digite sua idade: "))
  cidade = input("Digite sua cidade: ")

  users[nome] = {"age": idade, "city": cidade}
#3 - Ler um nome e se ele existir no dicionario, imprimir nome e idade
search = input("Digite o nome para buscar: ")
if search in users:
  print(f"Nome: {search} \nIdade: {users[search]['age']}")
#4 - Ler um nome e se ele existir no dicionario, editar a idade e cidade
edit = input("Digite o nome para editar: ")
if edit in users:
  new_age = int(input("Digite a nova idade: "))
  users[edit]["age"] = new_age
  new_city = input("Digite a nova cidade: ")
  users[edit]["city"] = new_city
  print(f"Usuario {edit} atualizado:\n Idade: {users[edit]['age']}\n Cidade: {users[edit]['city']}")
#5 - Remover um nome do dicionario
rem = input("Digite o nome para remover: ")
if rem in users:
  del users[rem]
  print(f"Usuario {rem} removido com sucesso!")
#6 - Imprimir o dicionario
print(users)