#Faça um programa que leia um numero inteiro e mostre o seu sucessor e antecessor.
def sucante(n):
    return n + 1, n - 1

num = int(input("Digite um numero inteiro: "))
suc, ante = sucante(num)
print(f"O sucessor de {num} é {suc} e o antecessor é {ante}.")