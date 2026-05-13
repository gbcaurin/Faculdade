x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 20]
for i in range(len(x)):
  maior = max(x)
  x.remove(maior)
  segundo_maior = max(x)
  break

print(f"O maior número é: {maior}")
print(f"O segundo maior número é: {segundo_maior}")