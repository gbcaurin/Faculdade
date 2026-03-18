#Leia o salario mensal de um funcionario e o percentual de reajuste e determine o valor do novo salario.
sal = float(input("Digite o valor do seu salario:"))
rea = float(input("Digite o percentual do reajuste do seu salario:"))
reatotal = rea / 100
total = sal * reatotal
totalsal = sal + total
print("O seu salario liquido é de:", totalsal)
