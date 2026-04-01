def even(a, b):
  even = 0
  for i in range(a, b+1):
    if i % 2 == 0:
      even += 1
      print(i)
  return print(f"Quantidade de números pares entre {a} e {b} é: {even}")

x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))
even(x, y)

