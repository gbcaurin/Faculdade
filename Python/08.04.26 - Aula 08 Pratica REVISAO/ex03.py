n = int(input("Digite quantos números voce quer somar de S: "))

S = 0
i = 2
c = 0

while c < n:
  S += i
  i += 3
  c += 1

print(f"A soma dos números é: {S}")