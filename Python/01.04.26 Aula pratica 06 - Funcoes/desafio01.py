def sumall(a, b):
  total = 0
  if a < b:
    for i in range(a, b+1):
      total += i
  else:
    for j in range(b, a+1):
      total += j
  return print(f"A soma dos números entre {a} e {b} é {total}")

x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))
sumall(x, y)