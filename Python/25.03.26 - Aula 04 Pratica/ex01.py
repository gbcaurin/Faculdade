""" 
DICA da Lucia: Fazer com While

c1 = 0
c2 = 0
c3 = 0
c4 = 0

n = int(input("Valor:"))

while n >= 0:
    if n < 25:
        c1 += 1
    elif n < 50:
        c2 += 1
    elif n < 75:
        c3 += 1
    else:
        c4 += 1
n = int(input("Valor:"))

print(f"Valores entre 0 e 24: {c1}")
print(f"Valores entre 25 e 49: {c2}")
print(f"Valores entre 50 e 74: {c3}")
print(f"Valores entre 75 e 100: {c4}") """

#como eu estava fazendo:

c1 = 0
c2 = 0
c3 = 0
c4 = 0

n = int(input("Quantidade de números:"))

for i in range(n):

    valor = int(input("Valor:"))
    if valor < 0 or valor > 100:
        print("Valor inválido. Encerrando o programa.")
        break
    else:
     if valor < 25:
        c1 += 1
     elif valor < 50:
        c2 += 1
     elif valor < 75:
        c3 += 1
     else:
        c4 += 1

print(f"Valores entre 0 e 24: {c1}")
print(f"Valores entre 25 e 49: {c2}")
print(f"Valores entre 50 e 74: {c3}")
print(f"Valores entre 75 e 100: {c4}")
