x = input("Digite seu nome: ")
y = input("Digite seu sexo (feminino/masculino): ")
z = int(input("Digite sua idade: "))

zl = y.lower()

if zl == "feminino" and z > 25:
  print(f"{x} aceita!")
else:
  print("Não aceita.")