#Calcular o reajuste de acordo com o salario.  
sal = float(input("Digite o valor do seu salário: "))
if sal >= 500:
  if sal >= 1000:
    reaj2 = sal * 0.05
    reaj1000 = sal + reaj2
    print("O valor do salário com reajuste adicional é:", reaj1000)
  else:
     reaj = sal * 0.10
     reaj500 = sal + reaj
     print("O valor do salário com reajuste é:", reaj500)
else:
  reaj3 = sal * 0.15
  reaj1 = sal + reaj3
  print("O valor do salário com reajuste é:", reaj1)