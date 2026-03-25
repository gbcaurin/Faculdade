x = int(input("Quantidade de numeros: "))
ip = 0
ii = 0
i = 0

while i < x:
  z = int(input("Digite um numero: "))
  if z % 2 == 0:
    ip += 1

  else:
    ii += 1
  i += 1
print(f"Numeros pares: {ip}")
print(f"Numeros impares: {ii}")