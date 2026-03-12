#Ler o valor de um produto, o valor do desconto em porcentagem e calcular o novo preco
val = float(input("Digite o valor do produto: "))
desc = int(input("Digite o valor do desconto em porcentagem: "))
porc = desc / 100
novo_preco = val - (val * porc)
print(f"O novo preço do produto com {desc}% de desconto é: R${novo_preco}")