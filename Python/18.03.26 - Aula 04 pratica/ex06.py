
n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite outro número inteiro: "))

print("O que voce deseja fazer com os números?")
print("1 - Media entre eles")
print("2 - Diferença do maior pelo menor")
print("3 - Multiplicar")
print("4 - Dividir")
opt = int(input("Digite a opção desejada: "))


if opt == 1:
  med = (n1 + n2) / 2
  print(f"A média entre {n1} e {n2} é: {med}")
elif opt == 2:
  if n1 > n2:
    diff = n1 - n2  
  else:
    diff = n2 - n1
  print(f"A diferença entre {n1} e {n2} é: {diff}")
elif opt == 3:
  mult = n1 * n2
  print(f"A multiplicação entre {n1} e {n2} é: {mult}")
elif opt == 4:
  div = n1 / n2
  print(f"{n1} dividido por {n2} é: {div}")
else:
  print("Digite uma opção valida")