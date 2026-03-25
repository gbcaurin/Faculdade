m1 = 0
m2 = 0
i = 0

while i < 10:
  x = int(input("Digite um numero: "))
  if x > m1:
    m2 = m1
    m1 = x
    i += 1
  elif x > m2:
    m2 = x
    i += 1
print(f"Os dois maiores numeros sao: {m1} e {m2}")
