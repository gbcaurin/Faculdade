arr = [12.5, 34.8, 27.1, 45.6, 19.9, 30.2, 8.7, 51.4, 29.3, 22.0]

med = sum(arr) / len(arr)

maior = 0
menor = 0
m29 = []
for i in arr:
    if i > maior:
        maior = i
    if menor == 0 or i < menor:
        menor = i
    if i > 29:
        m29.append(i)

print(f"Média: {med:.2f}")
print(f"Maior número: {maior}")
print(f"Menor número: {menor}")
print(f"Números maiores que 29:", *m29)
print("Numeros da lista: ", *arr)

