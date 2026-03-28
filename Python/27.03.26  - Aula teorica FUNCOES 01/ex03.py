def sumImposto (taxaI, custo):
  tx = taxaI / 100
  return custo + (custo * tx)

c = float(input("Digite o custo do produto: "))
t = float(input("Digite a taxa de imposto: "))
result = sumImposto(t, c)

print(f"O custo do produto com imposto é {result:.2f}.")