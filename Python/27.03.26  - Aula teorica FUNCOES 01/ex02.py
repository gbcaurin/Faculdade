#Faça um programa que leio um numero inteiro e uma função que some tres valores inteiros
def read(n):
    return print(f"O numero digitado foi {n}.")

def sum3(a , b, c):
    return print(f"A soma dos tres numeros é {a + b + c}.")

num = int(input("Digite um numero inteiro: "))
read(num)
x, y= map(int, input("Digite mais dois numeros inteiros separados por espaco: ").split())
sum3(num, x, y)