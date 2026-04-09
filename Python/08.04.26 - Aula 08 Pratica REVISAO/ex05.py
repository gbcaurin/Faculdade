x = int(input("Digite quantos numeros voce quer descobrir: "))

z = 0

for i in range(x):
  y = int(input("Digite o numero: "))
  if y <=1:
    print(f"{y} não é um número primo.")
  elif y == 2:
    print(f"{y} é um número primo.")
  else:
    for c in range(2, y):
      if y % c == 0:
        z += 1
    if z == 0:
      print(f"{y} é um número primo.")
    else:
      print(f"{y} não é um número primo.")

