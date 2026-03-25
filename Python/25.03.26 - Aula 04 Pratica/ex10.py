n = int(input("Digite um número inteiro: "))


while n >= 0:
    fat = 1
    for i in range(1, n + 1):
     fat = fat * i
    if n != 0:       
        print(f"O fatorial de {n} é: {fat}")
        n = int(input("Digite um número inteiro: "))
    else:
      print("O fatorial de 0 é: 1")
      n = int(input("Digite um número inteiro: "))
print("Programa encerrado.")