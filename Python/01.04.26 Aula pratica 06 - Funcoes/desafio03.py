def enum(n): # 6, 28, 496 e 8128
    soma = 0
    for i in range(1, n):
        if n % i == 0:
            soma += i
            
    if soma == n:
        print(f"{n} é perfeito")
    else:
        print(f"{n} não é perfeito")



x = int(input("Digite um numero: "))
enum(x)