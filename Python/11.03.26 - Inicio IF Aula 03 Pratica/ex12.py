#Descobrir se os numeros formam um triangulo, se sim, descobrir qual tipo de triangulo.  
a = int(input("Digite um número inteiro: "))
b = int(input("Digite outro número inteiro: "))
c = int(input("Digite mais um número inteiro: ")) 
if a < c+b and b < a+c and c < a+b:
  if a == b and b == c and a == c:
    print("Os números formam um triângulo equilátero.")
  if a == b and a != c or a == c and a != b or b == c and b != a:
    print("Os números formam um triângulo isósceles.")
  if a != b and a != c and b != c:
    print("Os números formam um triângulo escaleno.")
else:
  if a >= b+c:
    print(f"O número {a} é maior ou igual à soma de {b} e {c}, portanto não formam um triângulo.")
  if b >= a+c:
    print(f"O número {b} é maior ou igual à soma de {a} e {c}, portanto não formam um triângulo.")
  if c >= a+b:
    print(f"O número {c} é maior ou igual à soma de {a} e {b}, portanto não formam um triângulo.")