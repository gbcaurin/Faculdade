x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
z = []
for i in range(20):
  if x[i] % 3 == 0:
    print("Múltiplo de 3")
    z.append(x[i])
  else:
    print("Número não é múltiplo de 3")

print(f"Os múltiplos de 3 são: {z}")

    