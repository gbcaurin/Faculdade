#Pegar o salario bruto e o valor do emprestimo, se o valor do emprestimo for 30% do salario, recusar. Se nao aceitar. Se for cliente a mais de 2 anos,
#aceitar com bonus.   
sal = float(input("Digite o valor do seu salário: "))
emp = float(input("Digite o valor do seu empréstimo: "))
temp = int(input("Digite a quanto tempo voce presta serviço a empresa (em anos): "))
salemp = sal * 0.3
if emp < salemp:
  if temp > 2:
    print("Aprovado com bonus")
  else:
    print("Empréstimo aprovado")
else:
  print("Empréstimo não aprovado")