def read(n):
    return print(f"O numero digitado foi {n}.")

def sum3(a , b, c):
    return print(f"A soma dos tres numeros é {a + b + c}.")

num = int(input("Digite um numero inteiro: "))
read(num)
x, y, z = map(int, input("Digite tres numeros inteiros separados por espaco: ").split())
sum3(x, y, z)