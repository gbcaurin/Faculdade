i = []
p = []

n = int(input("Digite um número: "))
if n < 0:
  n = int(input("Digite um número positivo: "))
  if n % 2 == 0:
    p.append(n)
  else:
    i.append(n)

while n >= 0:
  n = int(input("Digite um número: "))
  if n > 0:
    if n % 2 == 0:
      p.append(n)
    else:
      i.append(n)

print(f"Os números pares são: {p}")
print(f"Os números ímpares são: {i}")