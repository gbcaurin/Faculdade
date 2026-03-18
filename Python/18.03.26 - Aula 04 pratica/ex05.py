x = int(input("Digite um número inteiro: "))
n = int(input("Digite um número inteiro para elevar o primeiro: "))

result = 1
saven = n

while n > 0:
    result *= x
    n -= 1

print(f"{x} elevado a {saven} é: {result}")







""" for _ in range(n):
    result *= x  """