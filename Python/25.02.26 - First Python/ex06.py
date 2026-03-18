#Faça um programa que dadas as medidas de uma sala em metro (comprimento e largura), bem como o preço do metro quadrado de carpete, informe o custo total
# para forrar o piso da sala.
larg = float(input("Digite a largura da sala em Metros:"))
compri = float(input("Digite o comprimento da sala em Metros:"))
area = larg * compri
precom2 = 7.5
custo = area * precom2
print("Voce ira gastar", custo,"Reais para preencher usa sala com carpete")