def entre(a, b):
  x = []
  for i in range(a, b):
    x.append(i)
  return x

def main():
  n = []
  y = int(input("Digite um número para lista(Digite um numero negativo para parar): "))
  while y >= 0:
    n.append(y)
    y = int(input("Digite um número para lista(Digite um numero negativo para parar): "))
  print(n)
  print(entre(1, 10))

main()