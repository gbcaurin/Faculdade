def sumnum(n):
  savex = n
  soma = 0
  while n > 0:
    soma += n % 10
    n //= 10
  return print(f"A soma dos digitos de {savex} é: {soma}")

def bigestnum(n):
  bigr = 0
  while n > 0:
    digit = n % 10
    if digit > bigr:
      bigr = digit
    n //= 10
  return print(f"O maior digito é: {bigr}")


x = int(input("Digite um numero: "))
sumnum(x)
bigestnum(x)
  


  
