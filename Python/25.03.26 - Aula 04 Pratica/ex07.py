w = 0
x = 0
y = int(input("Quantidade de numeros: "))
i = 0
ip = 0
ii = 0

mp = 0
mg = 0

while i < y:
  z = int(input("Digite um numero: "))
  if z % 2 == 0:
    ip += 1
    w += z
    mp = w / ip
  else:
    ii += 1
    x += z

  mg = (w + x) / y 
  i += 1

print(f"Numeros pares: {ip}")
print(f"Numeros impares: {ii}")
print(f"Media dos numeros pares: {mp}")
print(f"Media dos numeros: {mg}")
