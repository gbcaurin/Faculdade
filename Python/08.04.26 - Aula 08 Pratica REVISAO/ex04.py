q = int(input("Quantas pessoas ira participar?: "))
mpeso = 0
mfil = 0
ppmais100 = 0

for i in range(q):
  age = int(input("Digite a idade da pessoa: "))
  peso = float(input("Digite o peso da pessoa: "))
  filho = int(input("Digite o número de filhos da pessoa: "))

  mpeso += peso

  if peso >= 100:
    ppmais100 += 1

  if age >= 30 and age <= 40:
    mfil += filho

print(f" Média do peso da população: {mpeso/q}")
print(f" Média do número de filhos das pessoas com idade entre 30 e 40 anos: {mfil/q}")
print(f"Percentual de pessoas acima de 100kg: {ppmais100/q*100:.2f}%")
