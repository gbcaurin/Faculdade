x = input("Digite uma palavra: ")
y = input("Digite outra palavra: ")

if y in x[len(x)-len(y):]:
  print(f"{y} está no final de {x}")
else:
  print(f"{y} não está no final de {x}")