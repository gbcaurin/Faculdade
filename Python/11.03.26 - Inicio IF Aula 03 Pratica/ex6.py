#Se o produto for mais caro que 100 tem desconto de 10%, se nao, matem o mesmo preço.  
prod = float(input("Digite o valor do produto: "))
if prod > 100:
  desc = prod * 0.10
  valor = prod - desc
  print("O valor do produto com desconto é:", valor)
else:
  print("O valor do produto é:", prod)