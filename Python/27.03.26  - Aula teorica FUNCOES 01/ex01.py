def sucante(n):
    return n + 1, n - 1

num = int(input("Digite um numero inteiro: "))
suc, ante = sucante(num)
print(f"O sucessor de {num} é {suc} e o antecessor é {ante}.")