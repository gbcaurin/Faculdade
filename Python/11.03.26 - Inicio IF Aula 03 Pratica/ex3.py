#Receber dois numeros, se forem iguais, some, se for diferente multiplique.  
a = int(input("Digite um número inteiro: "))
b = int(input("Digite outro número inteiro: "))
if a == b:
  c = a+b
  print("A soma dos números é:", c)
else:
  d = a*b
  print("A multiplicação dos números é:", d)