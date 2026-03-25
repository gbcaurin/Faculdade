quest = int(input("Quantas pessoas irao participar?: "))
msal = 0
mfi = 0
maiorsal = 0
perc100 = 0

for i in range(quest):
    sal = int(input("Digite o salario da pessoa: "))
    fi = int(input("Digite o numero de filhos da pessoa: "))

    msal = msal + sal
    mfi = mfi + fi

    if sal > maiorsal:
        maiorsal = sal

    if sal > 100:
        perc100 += 1
print(f"Media salarial: {msal/quest}")
print(f"Media de filhos: {mfi/quest}")
print(f"Maior salario: {maiorsal}")
print(f"Percentual de pessoas com salario acima de 100: {(perc100/quest)*100}%")