m50 = 0
ta10a20 = 0
ma10a20 = 0
c10a20 = 0
percpm50 = 0
n = 25

for i in range(1, n+1):
  x = int(input("Digite sua idade: "))
  y = int(input("Digite sua altura em cm: "))
  z = int(input("Digite seu peso em kg: "))

  if x > 50:
    m50 += 1
  
  if x >= 10 and x <= 20:
    ta10a20 += y
    c10a20 += 1
    ma10a20 = ta10a20 / c10a20

  if z < 50:
    percpm50 += 1

print(f"Quantidade de pessoas com mais de 50 anos: {m50}")
print(f"Media de altura das pessoas entre 10 e 20 anos: {ma10a20}")
print(f"Percentual de pessoas com peso inferior a 50kg: {(percpm50/n)*100}%")

