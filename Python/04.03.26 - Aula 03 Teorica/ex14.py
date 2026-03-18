#Calular Comissao de Salario
sal = 1500
sellc = int(input("Digite quantos carros foram vendidos: "))
sell = float(input("Digite o valor de vendas: "))
comitc = sellc * 200
comit = sell * 0.05
salfinal = sal + comitc + comit
print(f"Salario Base: R${sal}\nComissão por carro vendido: R${comitc}\nComissão por valor de vendas: R${comit}\nSalário final: R${salfinal}")