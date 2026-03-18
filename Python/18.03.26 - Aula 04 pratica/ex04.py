print("Plano 1 - 10%")
print("Plano 2 - 15%")
print("Plano 3 - 20%")
plan = int(input("Digite o número do plano (1-3): "))
sal = float(input("Digite o salário: "))

if plan == 1:
  newsal = sal * 1.1
  print(f"Novo salário: {newsal}")
elif plan == 2:
  newsal = sal * 1.15
  print(f"Novo salário: {newsal}")
elif plan == 3:
  newsal = sal * 1.2
  print(f"Novo salário: {newsal}")
else:
  print("Plano inválido.")
