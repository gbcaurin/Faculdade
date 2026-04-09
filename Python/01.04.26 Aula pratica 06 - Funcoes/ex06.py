def fat(a):
  savea = a
  if a == 0:
    return print(f"{savea}! é 1")
  else:
    for i in range(a-1, 0, -1):
      a *= i
    return print(f"{savea}! é {a}")


x, y, z = map(int, input("Digite três números separados por espaço: ").split())
fat(x)
fat(y)
fat(z)