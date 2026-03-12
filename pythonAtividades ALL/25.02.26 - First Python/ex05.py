#Elabora um programa que dada uma distância percorrida (em km), bem como o total de combustivel gasto (em litros), informe o consumo do veiculo.
km = int(input("Digite quantos KMs você percorreu:"))
litro = int(input("Digite o total de combustivel gasto em Litros:"))
kmL = km // litro
print("O consumo do veiculo foi de:", kmL, "km/L")