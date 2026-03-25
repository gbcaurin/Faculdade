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
print(f"Valores entre 75 e 100: {c4}")